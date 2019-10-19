from functools import reduce
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    #program: decl+ EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        decls =[]
        for decl in ctx.decl():
            if decl.var_decl():
                decls = decls + self.visit(decl)
            else:
                decls.append(self.visit(decl))
        return Program(decls)

    #decl: var_decl|func_decl;
    def visitDecl(self,ctx:MCParser.DeclContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        if ctx.func_decl():
            return self.visit(ctx.func_decl())

    #var_decl: primitive_type list_id SM;
    #list_id: variable (CM variable)*;
    #variable: ID (LSB INTLIT RSB)?;
    def visitVar_decl(self,ctx:MCParser.Var_declContext):
        vardecl=[]
        variable = ctx.list_id().variable()
        for var in variable:
            if var.INTLIT():
                vardecl.append(VarDecl(Id(var.ID().getText()),ArrayType(IntLiteral(var.INTLIT().getText()),self.visit(ctx.primitive_type()))))
            else:
                vardecl.append(VarDecl(Id(var.ID().getText()),self.visit(ctx.primitive_type())))
        return vardecl

    #func_decl: (VOID|primitive_type|out_pointer) ID LB param_list? RB block_stmt;
    #param_list: param (CM param)*;
    #out_pointer: primitive_type LSB RSB;
    def visitFunc_decl(self,ctx:MCParser.Func_declContext):
        name = Id(ctx.ID().getText())
        param = ([self.visit(x) for x in ctx.param_list().param()] if ctx.param_list() else [])
        if ctx.VOID():
            type = VoidType()
        elif ctx.primitive_type():
            type =self.visit(ctx.primitive_type())
        else:
            if ctx.out_pointer().LSB():
                type = ArrayPointerType(self.visit(ctx.out_pointer().primitive_type()))
        body = self.visit(ctx.block_stmt())
        return FuncDecl(name,param,type,body)

    # param: primitive_type ID (LSB RSB)? ;
    def visitParam(self,ctx:MCParser.ParamContext):
        id = Id(ctx.ID().getText())
        type = self.visit(ctx.primitive_type())
        if ctx.LSB():
            return VarDecl(id,ArrayPointerType(type))
        else:
            return VarDecl(id,type)


    #block_stmt: LP (var_decl|stmt)* RP;
    def visitBlock_stmt(self,ctx: MCParser.Block_stmtContext):
        command = [];
        if ctx.var_decl():
            for decl in ctx.var_decl():
                command = command+self.visit(decl)
        if ctx.stmt():
            command = command + ([self.visit(x) for x in ctx.stmt()] if ctx.stmt() else [])
        return Block(command)
    
    #stmt: if_stmt|while_stmt|for_stmt|break_stmt|continue_stmt|return_stmt|expr_stmt|block_stmt;
    def visitStmt(self,ctx:MCParser.StmtContext):
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        if ctx.break_stmt():
            return Break()
        if ctx.continue_stmt():
            return Continue()
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        if ctx.expr_stmt():
            return self.visit(ctx.expr_stmt())
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        
    #if_stmt: IF LB expr RB stmt (ELSE stmt)?;
    def visitIf_stmt(self,ctx:MCParser.If_stmtContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.stmt(0))
        elseStmt = None
        if ctx.ELSE():
            elseStmt = self.visit(ctx.stmt(1))
        return If(expr,thenStmt,elseStmt)

    #while_stmt: DO stmt+ WHILE expr SM;
    def visitWhile_stmt(self,ctx:MCParser.While_stmtContext):
        sl = [self.visit(x) for x in ctx.stmt()]
        exp = self.visit(ctx.expr())
        return Dowhile(sl,exp)

    #for_stmt: FOR LB expr SM expr SM expr RB stmt;
    def visitFor_stmt(self,ctx:MCParser.For_stmtContext):
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        expr3 = self.visit(ctx.expr(2))
        loop = self.visit(ctx.stmt())
        return For(expr1,expr2,expr3,loop)
    
    #return_stmt: RETURN expr? SM;
    def visitReturn_stmt(self,ctx:MCParser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return()
    
    #expr_stmt: expr SM;
    def visitExpr_stmt(self,ctx:MCParser.Expr_stmtContext):
        return self.visit(ctx.expr())

    #func_call: ID LB (expr (CM expr)*)? RB;
    def visitFunc_call(self,ctx:MCParser.Func_callContext):
        id = Id(ctx.ID().getText())
        param = list(map(lambda x:self.visit(x),ctx.expr())) if ctx.expr() else []
        #param = ([self.visit(x) for x in ctx.expr()] if ctx.expr() else [])
        return CallExpr(id,param)

    # expr: expr1 ASSIGN expr
    # |expr1;
    def visitExpr(self,ctx:MCParser.ExprContext):
        if ctx.ASSIGN():
            op = ctx.ASSIGN().getText()
            left = self.visit(ctx.expr1())
            right = self.visit(ctx.expr())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.expr1())
    
    # expr1: expr1 OR expr2
    # |expr2;
    def visitExpr1(self,ctx:MCParser.Expr1Context):
        if ctx.OR():
            op = ctx.OR().getText()
            left = self.visit(ctx.expr1())
            right = self.visit(ctx.expr2())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.expr2())
    
    # expr2: expr2 AND expr3
    # |expr3;
    def visitExpr2(self,ctx:MCParser.Expr2Context):
        if ctx.AND():
            op = ctx.AND().getText()
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.expr3())
    
    # expr3: expr4 (EQUAL|NOT_EQUAL)expr4
    # |expr4;
    def visitExpr3(self,ctx:MCParser.Expr3Context):
        if ctx.EQUAL():
            op = ctx.EQUAL().getText()
        elif ctx.NOT_EQUAL():
            op = ctx.NOT_EQUAL().getText()
        else:
            return self.visit(ctx.expr4(0))
        left = self.visit(ctx.expr4(0))
        right = self.visit(ctx.expr4(1))
        return BinaryOp(op,left,right)
    
    # # expr4: expr5 (LESS_THAN|LESS_EQUAL|GREATER_EQUAL|GREATER_THAN) expr5
    # # |expr5;
    def visitExpr4(self,ctx:MCParser.Expr4Context):
        if ctx.LESS_THAN():
            op = ctx.LESS_THAN().getText()
        elif ctx.LESS_EQUAL():
            op = ctx.LESS_EQUAL().getText()
        elif ctx.GREATER_EQUAL():
            op = ctx.GREATER_EQUAL().getText()
        elif ctx.GREATER_THAN():
            op = ctx.GREATER_THAN().getText()
        else:
            return self.visit(ctx.expr5(0))
        left = self.visit(ctx.expr5(0))
        right = self.visit(ctx.expr5(1))
        return BinaryOp(op,left,right)
    
    # expr5: expr5 (ADD|SUB) expr6
    # |expr6;
    def visitExpr5(self,ctx:MCParser.Expr5Context):
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()
        else:
            return self.visit(ctx.expr6())
        left = self.visit(ctx.expr5())
        right = self.visit(ctx.expr6())
        return BinaryOp(op,left,right)

    # expr6: expr6 (DIV|MUL|MOD) expr7
    # |expr7;
    def visitExpr6(self,ctx:MCParser.Expr6Context):
        if ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()
        else:
            return self.visit(ctx.expr7())
        left = self.visit(ctx.expr6())
        right = self.visit(ctx.expr7())
        return BinaryOp(op,left,right)

    # expr7: (SUB|NOT) expr7
    # |expr8;
    def visitExpr7(self,ctx:MCParser.Expr7Context):
        if ctx.SUB():
            op = ctx.SUB().getText()
        elif ctx.NOT():
            op = ctx.NOT().getText()
        else:
            return self.visit(ctx.expr8())
        body = self.visit(ctx.expr7())
        return UnaryOp(op,body)
    
    # expr8: term LSB expr RSB|term;
    def visitExpr8(self,ctx:MCParser.Expr8Context):
        if ctx.LSB():
            arr = self.visit(ctx.term())
            idx = self.visit(ctx.expr())
            return ArrayCell(arr,idx)
        else:
            return self.visit(ctx.term())

    # term: BOOLLIT|FLOATLIT|INTLIT|STRINGLIT|ID|func_call|LB expr RB;
    def visitTerm(self,ctx:MCParser.TermContext):
        if ctx.BOOLLIT():
            return BooleanLiteral(bool(ctx.BOOLLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText()) 
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        else:
            return self.visit(ctx.expr())

    #primitive_type: INT|FLOAT|STRING|BOOLEAN;
    def visitPrimitive_type(self,ctx:MCParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return BoolType()
