import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_var_decl(self):
        input = """int a;"""
        expect = str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_var_decl1(self):
        input = """int a,b,c;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),\
                            VarDecl(Id("b"),IntType()),\
                            VarDecl(Id("c"),IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_var_decl2(self):
        input = """int a,b,c;
                    float x;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),\
                            VarDecl(Id("b"),IntType()),\
                            VarDecl(Id("c"),IntType()),\
                            VarDecl(Id("x"),FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_var_decl3(self):
        input = """int a,b,c[5];"""
        expect = str(Program([VarDecl(Id("a"),IntType()),\
                            VarDecl(Id("b"),IntType()),\
                            VarDecl(Id("c"),ArrayType(IntLiteral(5),IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_fucn_decl(self):
        input = """ void main(){} """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_fucn_decl1(self):
        input = """ void main(){int a;} """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),\
                                Block([VarDecl(Id("a"),IntType())]))
                                ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_func_decl2(self):
        input=""" int main(int a){float b;} """
        expect = str(Program([
                    FuncDecl(Id("main"),[VarDecl(Id("a"),IntType())],IntType(),Block([VarDecl(Id("b"),FloatType())]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_03(self):
        inp="""int a;"""
        out=str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.checkASTGen(inp,out,310))        
   
    def test_04(self):
        inp="""float arr,iNum,complex;"""
        out=str(Program([\
            VarDecl(Id("arr"),FloatType()),\
            VarDecl(Id("iNum"),FloatType()),\
            VarDecl(Id("complex"),FloatType())]))
        self.assertTrue(TestAST.checkASTGen(inp,out,311))        

    def test_05(self):
        inp="""float arr,iNum,str[2];"""
        out=str(Program([\
            VarDecl(Id("arr"),FloatType()),\
            VarDecl(Id("iNum"),FloatType()),\
            VarDecl(Id("str"), ArrayType(IntLiteral(2),FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,312))        

    def test_06(self):
        inp="""string str;
        string arr;
        string arr2D;
      """
        out=str(Program([\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("arr"),StringType()),\
            VarDecl(Id("arr2D"),StringType())]))
        self.assertTrue(TestAST.checkASTGen(inp,out,313))        

    def test_07(self):
        inp="""string str;
        int arr;
        float arr2D;
        boolean isTrue;
      """
        out=str(Program([\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("arr"),IntType()),\
            VarDecl(Id("arr2D"),FloatType()),\
            VarDecl(Id("isTrue"),BoolType())]))
        self.assertTrue(TestAST.checkASTGen(inp,out,314))        

    def test_08(self):
        inp="""string str,a2D[4];
        int arr,brr;
        float arr2D,arr3D[5];
        boolean isTrue,isFact;
      """
        out=str(Program([\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("a2D"),ArrayType(IntLiteral(4),StringType())),\
            VarDecl(Id("arr"),IntType()),\
            VarDecl(Id("brr"),IntType()),\
            VarDecl(Id("arr2D"),FloatType()),\
            VarDecl(Id("arr3D"),ArrayType(IntLiteral(5),FloatType())),\
            VarDecl(Id("isTrue"),BoolType()),\
            VarDecl(Id("isFact"),BoolType())]))
        self.assertTrue(TestAST.checkASTGen(inp,out,315))        
    
    def test_09(self):
        inp="""string str,a2D[4];
        string arr,brr;
        string arr2D,arr3D[5];
        string isTrue,isFact;
      """
        out=str(Program([\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("a2D"),ArrayType(IntLiteral(4),StringType())),\
            VarDecl(Id("arr"),StringType()),\
            VarDecl(Id("brr"),StringType()),\
            VarDecl(Id("arr2D"),StringType()),\
            VarDecl(Id("arr3D"),ArrayType(IntLiteral(5),StringType())),\
            VarDecl(Id("isTrue"),StringType()),\
            VarDecl(Id("isFact"),StringType())]))
        self.assertTrue(TestAST.checkASTGen(inp,out,316))        

    def test_10(self):
        inp="""boolean foo(){}"""
        out=str(Program([FuncDecl(Id("foo"),[],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,317))        
    
    def test_11(self):
        inp="""int main(){}
                  string getText(){}
                  boolean isEmptyString(){}
                  float isRealNumber(){}"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([])),\
            FuncDecl(Id("getText"),[],StringType(),Block([])),\
            FuncDecl(Id("isEmptyString"),[],BoolType(),Block([])),\
            FuncDecl(Id("isRealNumber"),[],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,318))        

    def test_12(self):
        inp="""int getSum(int Sum){}
                  string getText(string arr){}
                  boolean isEmptyString(string arr){}
                  float isRealNumber(float fNum){}"""
        out=str(Program([\
            FuncDecl(Id("getSum"),[VarDecl(Id("Sum"),IntType())],IntType(),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),StringType())],StringType(),Block([])),\
            FuncDecl(Id("isEmptyString"),[VarDecl(Id("arr"),StringType())],BoolType(),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),FloatType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,319))   

    def test_13(self):
        inp="""int getSum(int Sum, int count){}
                  string getText(string arr, int length){}
                  boolean isEmptyString(string arr, boolean isTrue){}
                  float isRealNumber(float fNum, float dNum, boolean isTrue){}"""
        out=str(Program([\
            FuncDecl(Id("getSum"),[VarDecl(Id("Sum"),IntType()),VarDecl(Id("count"),IntType())],IntType(),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),StringType()),VarDecl(Id("length"),IntType())],StringType(),Block([])),\
            FuncDecl(Id("isEmptyString"),[VarDecl(Id("arr"),StringType()),VarDecl(Id("isTrue"),BoolType())],BoolType(),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),FloatType()),VarDecl(Id("dNum"),FloatType()),VarDecl(Id("isTrue"),BoolType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,320))   

    def test_14(self):
        inp="""int getSum(int Sum, int count){}
                  string getText(string arr, int length){}
                  boolean isEmptyString(string arr, boolean isTrue){}
                  float isRealNumber(float fNum, float dNum, boolean isTrue){}"""
        out=str(Program([\
            FuncDecl(Id("getSum"),[VarDecl(Id("Sum"),IntType()),VarDecl(Id("count"),IntType())],IntType(),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),StringType()),VarDecl(Id("length"),IntType())],StringType(),Block([])),\
            FuncDecl(Id("isEmptyString"),[VarDecl(Id("arr"),StringType()),VarDecl(Id("isTrue"),BoolType())],BoolType(),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),FloatType()),VarDecl(Id("dNum"),FloatType()),VarDecl(Id("isTrue"),BoolType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,321))   
    
    def test_15(self):
        inp="""int getSum(int Sum, int count){}
                  string getText(string arr, int length){}
                  boolean isEmptyString(string arr, boolean isTrue){}
                  float isRealNumber(float fNum, float dNum, boolean isTrue){}"""
        out=str(Program([\
            FuncDecl(Id("getSum"),[VarDecl(Id("Sum"),IntType()),VarDecl(Id("count"),IntType())],IntType(),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),StringType()),VarDecl(Id("length"),IntType())],StringType(),Block([])),\
            FuncDecl(Id("isEmptyString"),[VarDecl(Id("arr"),StringType()),VarDecl(Id("isTrue"),BoolType())],BoolType(),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),FloatType()),VarDecl(Id("dNum"),FloatType()),VarDecl(Id("isTrue"),BoolType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,322))
    
    def test_16(self):
        inp="""int getSum(int Sum[]){}
                  string getText(string arr[]){}
                  boolean isEmptyString(string arr[]){}
                  float isRealNumber(float fNum[]){}"""
        out=str(Program([\
            FuncDecl(Id("getSum"),[VarDecl(Id("Sum"),ArrayPointerType(IntType()))],IntType(),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),ArrayPointerType(StringType()))],StringType(),Block([])),\
            FuncDecl(Id("isEmptyString"),[VarDecl(Id("arr"),ArrayPointerType(StringType()))],BoolType(),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),ArrayPointerType(FloatType()))],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,323))   
    
    def test_17(self):
        inp="""int getSum(int Sum[], int count[]){}
                   string getText(string arr[], int length[]){}
                   boolean isEmptyString(string arr[], boolean isTrue[]){}
                  float isRealNumber(float fNum[], float dNum[], boolean isTrue[]){}"""
        out=str(Program([\
            FuncDecl(Id("getSum"),[VarDecl(Id("Sum"),ArrayPointerType(IntType())),VarDecl(Id("count"),ArrayPointerType(IntType()))],IntType(),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),ArrayPointerType(StringType())),VarDecl(Id("length"),ArrayPointerType(IntType()))],StringType(),Block([])),\
            FuncDecl(Id("isEmptyString"),[VarDecl(Id("arr"),ArrayPointerType(StringType())),VarDecl(Id("isTrue"),ArrayPointerType(BoolType()))],BoolType(),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),ArrayPointerType(FloatType())),VarDecl(Id("dNum"),ArrayPointerType(FloatType())),VarDecl(Id("isTrue"),ArrayPointerType(BoolType()))],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,324))   

    def test_18(self):
        inp="""int getSum(int Sum[], int count){}
                   string getText(string arr[], int length){}
                   boolean isEmptyString(string arr[], boolean isTrue){}
                  float isRealNumber(float fNum[], float dNum, boolean isTrue[]){}"""
        out=str(Program([\
            FuncDecl(Id("getSum"),[VarDecl(Id("Sum"),ArrayPointerType(IntType())),VarDecl(Id("count"),IntType())],IntType(),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),ArrayPointerType(StringType())),VarDecl(Id("length"),IntType())],StringType(),Block([])),\
            FuncDecl(Id("isEmptyString"),[VarDecl(Id("arr"),ArrayPointerType(StringType())),VarDecl(Id("isTrue"),BoolType())],BoolType(),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),ArrayPointerType(FloatType())),VarDecl(Id("dNum"),FloatType()),VarDecl(Id("isTrue"),ArrayPointerType(BoolType()))],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,325))

    def test_19(self):
        inp="""int[] foo(){}
                  string[] getText(){}
                  float[] isRealNumber(){}"""
        out=str(Program([\
            FuncDecl(Id("foo"),[],ArrayPointerType(IntType()),Block([])),\
            FuncDecl(Id("getText"),[],ArrayPointerType(StringType()),Block([])),\
            FuncDecl(Id("isRealNumber"),[],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,326))
    
    def test_20(self):
        input="""int[] foo(int number){}
                  string[] getText(string arr){}
                  float[] isRealNumber(float fNum){}"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("number"),IntType())],ArrayPointerType(IntType()),Block([])),\
                    FuncDecl(Id("getText"),[VarDecl(Id("arr"),StringType())],ArrayPointerType(StringType()),Block([])),\
                    FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),FloatType())],ArrayPointerType(FloatType()),Block([]))\
                    ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_21(self):
        input="""int x[3];
                int[] foo(int a[]){}"""
        expect=str(Program([\
                VarDecl(Id("x"),ArrayType(IntLiteral(3),IntType())),\
                FuncDecl(Id("foo"),[VarDecl(Id("a"),ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([]))\
                ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_22(self):
        inp="""int[] foo(int number[]){}
                  string[] getText(string arr[]){}
                  float[] isRealNumber(float fNum[]){}"""
        out=str(Program([\
            FuncDecl(Id("foo"),[VarDecl(Id("number"),ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),ArrayPointerType(FloatType()))],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,329))    

    def test_23(self):
        inp="""int[] foo(int number[], int iNum[]){}
                  string[] getText(string arr[], string length[]){}
                  float[] isRealNumber(float fNum[], boolean isTrue[]){}"""
        out=str(Program([\
            FuncDecl(Id("foo"),[VarDecl(Id("number"),ArrayPointerType(IntType())),VarDecl(Id("iNum"),ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),ArrayPointerType(StringType())),VarDecl(Id("length"),ArrayPointerType(StringType()))],ArrayPointerType(StringType()),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),ArrayPointerType(FloatType())),VarDecl(Id("isTrue"),ArrayPointerType(BoolType()))],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,330))  
    
    def test_24(self):
        inp="""int[] getSum(int Sum[], int count){}
                   string[] getText(string arr[], int length){}
                  float[] isRealNumber(float fNum[], float dNum, boolean isTrue[]){}"""
        out=str(Program([\
            FuncDecl(Id("getSum"),[VarDecl(Id("Sum"),ArrayPointerType(IntType())),VarDecl(Id("count"),IntType())],ArrayPointerType(IntType()),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),ArrayPointerType(StringType())),VarDecl(Id("length"),IntType())],ArrayPointerType(StringType()),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),ArrayPointerType(FloatType())),VarDecl(Id("dNum"),FloatType()),VarDecl(Id("isTrue"),ArrayPointerType(BoolType()))],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,331))

    def test_27(self):
        inp="""int[] getSum(int Sum[], int size){}
                   string getText(string arr[], int length){}
                   float isRealNumber(float fNum[], boolean isFalse){}
                   boolean[] isFact(boolean isTrue[], int size){}"""
        out=str(Program([\
            FuncDecl(Id("getSum"),[VarDecl(Id("Sum"),ArrayPointerType(IntType())),VarDecl(Id("size"),IntType())],ArrayPointerType(IntType()),Block([])),\
            FuncDecl(Id("getText"),[VarDecl(Id("arr"),ArrayPointerType(StringType())),VarDecl(Id("length"),IntType())],StringType(),Block([])),\
            FuncDecl(Id("isRealNumber"),[VarDecl(Id("fNum"),ArrayPointerType(FloatType())),VarDecl(Id("isFalse"),BoolType())],FloatType(),Block([])),\
            FuncDecl(Id("isFact"),[VarDecl(Id("isTrue"),ArrayPointerType(BoolType())),VarDecl(Id("size"),IntType())],ArrayPointerType(BoolType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,332))
    
    def test_29(self):
        inp="""void main(){}
        int foo(){}
        int iNum;
        string str;
        boolean isTrue;"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([])),\
            FuncDecl(Id("foo"),[],IntType(),Block([])),\
            VarDecl(Id("iNum"),IntType()),\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("isTrue"),BoolType())]))
        self.assertTrue(TestAST.checkASTGen(inp,out,333))

    def test_30(self):
        inp="""void main(){}
         int max_size;
        int foo(){}
        int iNum;
        string str;
        boolean isTrue;
        int maxStr(string str){}"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([])),\
            VarDecl(Id("max_size"),IntType()),\
            FuncDecl(Id("foo"),[],IntType(),Block([])),\
            VarDecl(Id("iNum"),IntType()),\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("isTrue"),BoolType()),\
            FuncDecl(Id("maxStr"),[VarDecl(Id("str"),StringType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,334))

    def test_33(self):
        inp="""int iNum, max_level[5];
        string str,arr;
        boolean isTrue, isFact[5];
        void main(){}
        int foo(){}"""
        out=str(Program([\
            VarDecl(Id("iNum"),IntType()),\
            VarDecl(Id("max_level"),ArrayType(IntLiteral(5),IntType())),\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("arr"),StringType()),\
            VarDecl(Id("isTrue"),BoolType()),\
            VarDecl(Id("isFact"),ArrayType(IntLiteral(5),BoolType())),\
            FuncDecl(Id("main"),[],VoidType(),Block([])),\
            FuncDecl(Id("foo"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,335))

    def test_42(self):
        inp="""int main(){
        int iNum;
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("iNum"),IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,336)) 

    def test_43(self):
        inp="""int main(){
        int iNum, size, length;
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("iNum"),IntType()),VarDecl(Id("size"),IntType()),VarDecl(Id("length"),IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,337))

    def test_44(self):
        inp="""int main(){
        int iNum, size, length;
        string str;
        boolean isFact;
        float fNum;
        }"""
        out=str(Program([FuncDecl(Id("main"),[],IntType(),\
                Block([VarDecl(Id("iNum"),IntType()),\
                    VarDecl(Id("size"),IntType()),\
                    VarDecl(Id("length"),IntType()),\
                    VarDecl(Id("str"),StringType()),\
                    VarDecl(Id("isFact"),BoolType()),\
                    VarDecl(Id("fNum"),FloatType())]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,338))

    def test_45(self):
        inp="""int main(){
        int iNum, size, length;
        string str[10];
        boolean isFact;
        float fNum, number[5];
        int arr[10];
        }"""
        out=str(Program([FuncDecl(Id("main"),[],IntType(),\
            Block([VarDecl(Id("iNum"),IntType()),\
                VarDecl(Id("size"),IntType()),\
                VarDecl(Id("length"),IntType()),\
                VarDecl(Id("str"),ArrayType(IntLiteral(10),StringType())),\
                VarDecl(Id("isFact"),BoolType()),\
                VarDecl(Id("fNum"),FloatType()),\
                VarDecl(Id("number"),ArrayType(IntLiteral(5),FloatType())),\
                VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType()))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,339))

    def test_funcall46(self):
        inp="void main () {foo();}"
        out=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,340))

    def test_funcall47(self):
        inp="void main () {foo(25);}"
        out=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(25)])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,341))

    def test_funcall48(self):
        inp="void main () {foo(arr, iNum, max, min);}"
        out=str(Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[Id("arr"),Id("iNum"),Id("max"),Id("min")])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,342))

    def test_funcall49(self):
        inp="""void main () {compare(arr[10]);}"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),\
                Block([CallExpr(Id("compare"),[ArrayCell(Id("arr"),IntLiteral(10))])]))]))  
        self.assertTrue(TestAST.checkASTGen(inp,out,343))

    def test_92(self):
        inp="""int MAX_SIZE;
      int sum;
      void swap(int a, int b){
        int c;
        c = a;
        a = b;
        b = c;  
      }
      int main(){
        int a, b;
        swap(a,b);
        println(a,b);
      }"""

        out = str(Program([VarDecl(Id("MAX_SIZE"),IntType()),VarDecl(Id("sum"),IntType()),\
                FuncDecl(Id("swap"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],\
                VoidType(),Block([VarDecl(Id("c"),IntType()),BinaryOp("=",Id("c"),Id("a")),\
                BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("c"))])),\
                FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),\
                VarDecl(Id("b"),IntType()),CallExpr(Id("swap"),[Id("a"),Id("b")]),\
                CallExpr(Id("println"),[Id("a"),Id("b")])]))]))
        #out=str(Program([VarDecl(Id("MAX_SIZE"),IntType()),VarDecl(Id("sum"),IntType()),FuncDecl(Id("swap"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),Block([VarDecl(Id("c"),IntType())],[BinaryOp("=",Id("c"),Id("a")),BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("c"))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[CallExpr(Id("swap"),[Id("a"),Id("b")]),CallExpr(Id("println"),[Id("a"),Id("b")])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,344))

    def test_funcall50(self):
        input = """int main(){
                foo(i[a[3]]);
        }"""
        expect=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo"),[ArrayCell(Id("i"),ArrayCell(Id("a"),IntLiteral(3)))])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_funcall51(self):
        input ="""void main(){
            foo(a[i[3]+3]);
        }"""
        expect=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[ArrayCell(Id("a"),BinaryOp("+",ArrayCell(Id("i"),IntLiteral(3)),IntLiteral(3)))])]))\
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_funcall52(self):
        input="""void main(){
            foo(a(3));
        }"""
        expect=str(Program([
            FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[CallExpr(Id("a"),[IntLiteral(3)])])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_funcall53(self):
        input="""void main(){
            foo(f(a,3));
        }"""
        expect = str(Program([
            FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[CallExpr(Id("f"),[Id("a"),IntLiteral(3)])])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_whilestmt50(self):
        inp="""void main () {
          do{
            int a;
          } while true;
         }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([VarDecl(Id("a"),IntType())])],BooleanLiteral(True))]))\
                ]))
        self.assertTrue(TestAST.checkASTGen(inp,out,349))

    def test_while51(self):
        inp="""void main () {
        do{
         int a;
         string arr[10];
         int lengthStr, size;
         } while (a!=b);}"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),\
            Block([Dowhile([Block([VarDecl(Id("a"),IntType()),\
            VarDecl(Id("arr"),ArrayType(IntLiteral(10),StringType())),\
            VarDecl(Id("lengthStr"),IntType()),VarDecl(Id("size"),IntType())])],\
            BinaryOp("!=",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,350))  

    def test_while52(self):
        inp="""void main () {
        do{
         a = a + 3;
         isTrue = 3 > 5;
         a*(b+5)/15*(9*8*7*arr);
         } while (a!=b);}"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),\
            Block([Dowhile([Block([BinaryOp("=",Id("a"),\
            BinaryOp("+",Id("a"),IntLiteral(3))),\
            BinaryOp("=",Id("isTrue"),\
            BinaryOp(">",IntLiteral(3),IntLiteral(5))),\
            BinaryOp("*",BinaryOp("/",BinaryOp("*",Id("a"),\
            BinaryOp("+",Id("b"),IntLiteral(5))),IntLiteral(15)),\
            BinaryOp("*",BinaryOp("*",BinaryOp("*",IntLiteral(9),IntLiteral(8)),IntLiteral(7)),Id("arr")))])],\
            BinaryOp("!=",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,352))

    def test_if53(self):
        input="""void main () {
        if(a>5){
         fNum = 1.2e-2;
        }
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),\
                Block([If(BinaryOp(">",Id("a"),IntLiteral(5)),\
                Block([BinaryOp("=",Id("fNum"),FloatLiteral("0.012"))]),None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_if54(self):
        input="""void main () {
          if(a>5){
           fNum = 1.5e-2;
           arr[10] = 15+5*2/10;
           foo(2)[20] = 25+arr[10];
          }
        }"""

        expect = str(Program([\
                FuncDecl(Id("main"),[],VoidType(),Block([\
                    If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([\
                        BinaryOp("=",Id("fNum"),FloatLiteral(float(0.015))),\
                        BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(10)),\
                        BinaryOp("+",IntLiteral(15),\
                        BinaryOp("/",BinaryOp("*",IntLiteral(5),IntLiteral(2)),IntLiteral(10)))),\
                        BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(20)),\
                        BinaryOp("+",IntLiteral(25),ArrayCell(Id("arr"),IntLiteral(10))))\
                    ]),None)
                ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_ifdo55(self):
        inp="""void main () {
          if(a>5){
           do{
           a= a+5;
           foo(2);
           }while (a!=100);
          }
        }"""
        expect= str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([\
                If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([\
                    Dowhile([Block([\
                        BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(5))),\
                        CallExpr(Id("foo"),[IntLiteral(2)])\
                    ])],BinaryOp("!=",Id("a"),IntLiteral(100)))\
                ]),None)
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(inp,expect,355))
    
    def test_ifdo56(self):
        inp="""void main () {
          if(a>5){
             int arr[10];
             string str, charStr;
             boolean isTrue, isFact, isFalse;
             float fNum;
             do{
               a= a+5;
               foo(2);
             }while (a!=100);
          }
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([\
                If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([\
                    VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),\
                    VarDecl(Id("str"),StringType()),VarDecl(Id("charStr"),StringType()),\
                    VarDecl(Id("isTrue"),BoolType()),VarDecl(Id("isFact"),BoolType()),\
                    VarDecl(Id("isFalse"),BoolType()),VarDecl(Id("fNum"),FloatType()),\
                    Dowhile([Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(5))),\
                    CallExpr(Id("foo"),[IntLiteral(2)])])],\
                    BinaryOp("!=",Id("a"),IntLiteral(100)))]),None)]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,356))

    def test_ifelse57(self):
        inp="""void main () {
        if(a>5){
         fNum = 1.3e-2;
        }
        else{
          fNum = 2.3e-2;
        }
        }"""
        out=str(Program([\
                    FuncDecl(Id("main"),[],VoidType(),Block(\
                        [If(BinaryOp(">",Id("a"),IntLiteral(5)),\
                                Block([BinaryOp("=",Id("fNum"),FloatLiteral(float(0.013)))])\
                        ,(Block([BinaryOp("=",Id("fNum"),FloatLiteral(float(0.023)))])))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,357))

    def test_58(self):
        inp="""void main () {
          if(a>5){
            fNum = 1.3e-2;
            arr[10] = 15+5*2/10;
            foo(2)[20] = 25+arr[10];
          }
          else{
            fNum = 2.3e-2;
            arr[10] = 0;
            foo(2)[20] = 25+arr[10];
          }
        }"""
        expect = str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([\
                If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([\
                    BinaryOp("=",Id("fNum"),FloatLiteral(float(0.013))),\
                    BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(10)),\
                        BinaryOp("+",IntLiteral(15),\
                            BinaryOp("/",BinaryOp("*",IntLiteral(5),IntLiteral(2)),IntLiteral(10))\
                        )),\
                    BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(20)),\
                        BinaryOp("+",IntLiteral(25),ArrayCell(Id("arr"),IntLiteral(10))))\
                ]),\
                Block([\
                    BinaryOp("=",Id("fNum"),FloatLiteral(float(0.023))),\
                    BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(10)),IntLiteral(0)),\
                    BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(20)),\
                        BinaryOp("+",IntLiteral(25),ArrayCell(Id("arr"),IntLiteral(10))))\
                ]))
            ]))    
        ]))
        self.assertTrue(TestAST.checkASTGen(inp,expect,358))

    def test_59(self):
        inp="""void main () {
          if(a>5){
            do{
              a= a+5;
              foo(2);
            }while (a!=100);
          }
          else{
            do{
              a = a * 2;
              compare(a,max);
            }while (a!=144);
          }
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([\
                If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([\
                    Dowhile([Block([BinaryOp("=",Id("a"),\
                        BinaryOp("+",Id("a"),IntLiteral(5))),\
                        CallExpr(Id("foo"),[IntLiteral(2)])])],\
                        BinaryOp("!=",Id("a"),IntLiteral(100)))]),Block([\
                        Dowhile([Block([BinaryOp("=",Id("a"),\
                        BinaryOp("*",Id("a"),IntLiteral(2))),\
                        CallExpr(Id("compare"),[Id("a"),Id("max")])])],\
                        BinaryOp("!=",Id("a"),IntLiteral(144)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,359))

    def test_dowhile60(self):
        input = """float main(){
            do
                a = 1;
                {
                    foo(3,2);
                    a = arr[2];
                }
            while(a);
        }"""
        expect = str(Program([\
                FuncDecl(Id("main"),[],FloatType(),Block([\
                    Dowhile([BinaryOp("=",Id("a"),IntLiteral(1)),Block([\
                        CallExpr(Id("foo"),[IntLiteral(3),IntLiteral(2)]),\
                        BinaryOp("=",Id("a"),ArrayCell(Id("arr"),IntLiteral(2)))\
                    ])],Id("a"))\
                ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_dowhile61(self):
        input = """float main(){
            do
                a = 1;
                b = true;
                {
                    foo(3,2);
                    a = arr[2];
                }
            while(a);
        }"""
        expect = str(Program([\
                FuncDecl(Id("main"),[],FloatType(),Block([\
                    Dowhile([BinaryOp("=",Id("a"),IntLiteral(1)),\
                        BinaryOp("=",Id("b"),BooleanLiteral(True)),Block([\
                        CallExpr(Id("foo"),[IntLiteral(3),IntLiteral(2)]),\
                        BinaryOp("=",Id("a"),ArrayCell(Id("arr"),IntLiteral(2)))\
                    ])],Id("a"))\
                ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    
    def test_ifwhile62(self):
        inp="""void main () {
          if(a>5){
             int arr[10];
             do{
               a= a+5;
               foo(2);
             }while (a!=100);
          }
          else{
            int arr[10];
            do{
              a= a*2;
              compare(a, max);
            }while (a!=144);
          }
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([\
                If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([\
                VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),\
                Dowhile([Block([BinaryOp("=",Id("a"),\
                BinaryOp("+",Id("a"),IntLiteral(5))),\
                CallExpr(Id("foo"),[IntLiteral(2)])])],\
                BinaryOp("!=",Id("a"),IntLiteral(100)))]),Block([\
                VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),Dowhile([Block([\
                BinaryOp("=",Id("a"),BinaryOp("*",Id("a"),IntLiteral(2))),\
                CallExpr(Id("compare"),[Id("a"),Id("max")])])],\
                BinaryOp("!=",Id("a"),IntLiteral(144)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,362))
    
    def test_bulkif61(self):
        inp="""void main () {
          if(a>5){
            if(a!=prime){
              foo(a);
            }
          }
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([\
                If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([\
                    If(BinaryOp("!=",Id("a"),Id("prime")),Block([\
                        CallExpr(Id("foo"),[Id("a")])]),None)]),None)]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,363)) 

    def test_bulkif62(self):
        inp="""void main () {
          if(a>5)
            if(a!=prime)
              if(a%15==1)
                if(a<100)
                  foo(a,max);
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([\
                If(BinaryOp(">",Id("a"),IntLiteral(5)),\
                    If(BinaryOp("!=",Id("a"),Id("prime")),\
                        If(BinaryOp("==",BinaryOp("%",Id("a"),IntLiteral(15)),IntLiteral(1)),\
                            If(BinaryOp("<",Id("a"),IntLiteral(100)),\
                                CallExpr(Id("foo"),[Id("a"),Id("max")]),None),None),None),None)]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,364))

    def test_63(self):
        inp="""void main () {
          if(a>5){
            if(a!=prime){
              foo(a);
            }
          }
          else{
            if(a==fact(10)){
              foo(fact(10));
            }
          }
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([\
                If(BinaryOp(">",Id("a"),IntLiteral(5)),Block([\
                    If(BinaryOp("!=",Id("a"),Id("prime")),Block([\
                        CallExpr(Id("foo"),[Id("a")])]),None)]),Block([\
                            If(BinaryOp("==",Id("a"),\
                                CallExpr(Id("fact"),[IntLiteral(10)])),Block([\
                                    CallExpr(Id("foo"),\
                                        [CallExpr(Id("fact"),[IntLiteral(10)])])]),None)]))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,365))

    def test_for66(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){}
        }"""
        expect = str(Program([\
                FuncDecl(Id("main"),[],IntType(),Block([\
                    For(BinaryOp("=",Id("i"),IntLiteral(0)),\
                        BinaryOp("<",Id("i"),Id("iNum")),\
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),\
                        Block([]))\
                ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(inp,expect,366))

    def test_for67(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){
              foo(3);
          }
        }"""
        expect = str(Program([\
                FuncDecl(Id("main"),[],IntType(),Block([\
                    For(BinaryOp("=",Id("i"),IntLiteral(0)),\
                        BinaryOp("<",Id("i"),Id("iNum")),\
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),\
                        Block([CallExpr(Id("foo"),[IntLiteral(3)])]))\
                ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(inp,expect,367))

    def test_for68(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){
              foo(a[3]);
              max(a[3],b[3]);
          }
        }"""
        expect = str(Program([\
                FuncDecl(Id("main"),[],IntType(),Block([\
                    For(BinaryOp("=",Id("i"),IntLiteral(0)),\
                        BinaryOp("<",Id("i"),Id("iNum")),\
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),\
                        Block([CallExpr(Id("foo"),[ArrayCell(Id("a"),IntLiteral(3))]),\
                        CallExpr(Id("max"),[ArrayCell(Id("a"),IntLiteral(3)),\
                        ArrayCell(Id("b"),IntLiteral(3))])]))\
                ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(inp,expect,368))

    def test_68(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){
            if(i%2==0){
              println(i);
            }
            else{
              do{
                iNum = iNum - i;
                foo(iNum%i);
                println(iNum);
              } while (iNum > pow(i,4));
            }
          }
         }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([\
                For(BinaryOp("=",Id("i"),IntLiteral(0)),\
                    BinaryOp("<",Id("i"),Id("iNum")),\
                    BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),Block([\
                    If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([\
                    CallExpr(Id("println"),[Id("i")])]),Block([\
                    Dowhile([Block([BinaryOp("=",Id("iNum"),\
                    BinaryOp("-",Id("iNum"),Id("i"))),CallExpr(Id("foo"),\
                    [BinaryOp("%",Id("iNum"),Id("i"))]),CallExpr(Id("println"),\
                    [Id("iNum")])])],BinaryOp(">",Id("iNum"),CallExpr(Id("pow"),\
                    [Id("i"),IntLiteral(4)])))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,369))

    def test_buldfor69(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){
            for(j=0;j<i;j=j+1){
              foo(i,j,max(i*j,iNum));
            }
          }
         }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([\
            For(BinaryOp("=",Id("i"),IntLiteral(0)),\
                BinaryOp("<",Id("i"),Id("iNum")),BinaryOp("=",Id("i"),\
                BinaryOp("+",Id("i"),IntLiteral(2))),Block([\
                For(BinaryOp("=",Id("j"),IntLiteral(0)),\
                BinaryOp("<",Id("j"),Id("i")),BinaryOp("=",Id("j"),\
                BinaryOp("+",Id("j"),IntLiteral(1))),Block([\
                CallExpr(Id("foo"),[Id("i"),Id("j"),\
                CallExpr(Id("max"),[BinaryOp("*",Id("i"),Id("j")),Id("iNum")])])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,370))

    def test_70(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){
            for(j=0;j<i;j=j+1){
              for(k=0;k<j; k= k+1){
                for(l=0;l<k;l=l+2){
                  getText(i,j,k,l);
                }
              }
            }
          }
         }"""
        out=str(Program([FuncDecl(Id("main"),[],IntType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("iNum")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("i")),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([For(BinaryOp("=",Id("k"),IntLiteral(0)),BinaryOp("<",Id("k"),Id("j")),BinaryOp("=",Id("k"),BinaryOp("+",Id("k"),IntLiteral(1))),Block([For(BinaryOp("=",Id("l"),IntLiteral(0)),BinaryOp("<",Id("l"),Id("k")),BinaryOp("=",Id("l"),BinaryOp("+",Id("l"),IntLiteral(2))),Block([CallExpr(Id("getText"),[Id("i"),Id("j"),Id("k"),Id("l")])]))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,371))

    def test_break71(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){
              break;
          }
        }"""
        expect = str(Program([\
                FuncDecl(Id("main"),[],IntType(),Block([\
                    For(BinaryOp("=",Id("i"),IntLiteral(0)),\
                        BinaryOp("<",Id("i"),Id("iNum")),\
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),\
                        Block([Break()]))\
                ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(inp,expect,372))

    def test_continue72(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){
              continue;
          }
        }"""
        expect = str(Program([\
                FuncDecl(Id("main"),[],IntType(),Block([\
                    For(BinaryOp("=",Id("i"),IntLiteral(0)),\
                        BinaryOp("<",Id("i"),Id("iNum")),\
                        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),\
                        Block([Continue()]))\
                ]))
            ]))
        self.assertTrue(TestAST.checkASTGen(inp,expect,373))

    def test_71(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){
            k = foo(i,pow(i,3));
            if(k>144){
              break;
            }
            else{
              continue;
            }
            println(k);
          }
         }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([\
            For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("iNum")),\
            BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),Block([\
            BinaryOp("=",Id("k"),CallExpr(Id("foo"),[Id("i"),\
            CallExpr(Id("pow"),[Id("i"),IntLiteral(3)])])),\
            If(BinaryOp(">",Id("k"),IntLiteral(144)),Block([\
            Break()]),Block([Continue()])),CallExpr(Id("println"),[Id("k")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,374))

    def test_72(self):
        inp="""int main(){
          for(i=0;i<iNum;i=i+2){
            k = foo(i,pow(i,3));
            if(k>144){
              break;
            }
            else{
              continue;
            }
            if(i==prime){
              return 0;
            }
            println(k);
          }
         }"""
        out=str(Program([\
        FuncDecl(Id("main"),[],IntType(),Block([\
        For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("iNum")),\
        BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),Block([\
        BinaryOp("=",Id("k"),CallExpr(Id("foo"),[Id("i"),\
        CallExpr(Id("pow"),[Id("i"),IntLiteral(3)])])),\
        If(BinaryOp(">",Id("k"),IntLiteral(144)),Block([\
        Break()]),Block([Continue()])),If(BinaryOp("==",Id("i"),Id("prime")),Block([\
        Return(IntLiteral(0))]),None),CallExpr(Id("println"),[Id("k")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,375))
    
    def test_73(self):
        inp="""void main(){
             int i;
             ramdon(i);
             if(i>10){
               break;
             }
             else{
               println(i);
               goto(ramdon(i));
             }
             return ;
            }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],VoidType(),Block([VarDecl(Id("i"),IntType()),\
            CallExpr(Id("ramdon"),[Id("i")]),\
            If(BinaryOp(">",Id("i"),IntLiteral(10)),Block([\
            Break()]),Block([CallExpr(Id("println"),[Id("i")]),\
            CallExpr(Id("goto"),[CallExpr(Id("ramdon"),[Id("i")])])])),Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,376))

    def test_76(self):
        inp="""int foo(int arr[], int iNum, boolean isTrue){
          isTrue = iNum %2;
          arr[0] = iNum %6;
          iNum = iNum + 19;
          arr[1] = arr[0] + iNum;
          foo(arr, iNum, isTrue);
          return iNum;
        }"""
        out=str(Program([\
            FuncDecl(Id("foo"),[VarDecl(Id("arr"),ArrayPointerType(IntType())),\
                VarDecl(Id("iNum"),IntType()),VarDecl(Id("isTrue"),\
                BoolType())],IntType(),Block([\
                BinaryOp("=",Id("isTrue"),BinaryOp("%",Id("iNum"),IntLiteral(2))),\
                BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(0)),\
                BinaryOp("%",Id("iNum"),IntLiteral(6))),BinaryOp("=",Id("iNum"),\
                BinaryOp("+",Id("iNum"),IntLiteral(19))),\
                BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(1)),\
                BinaryOp("+",ArrayCell(Id("arr"),IntLiteral(0)),Id("iNum"))),\
                CallExpr(Id("foo"),[Id("arr"),Id("iNum"),Id("isTrue")]),Return(Id("iNum"))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,377))

    def test_79(self):
        inp="""int foo(int arr[], int iNum, boolean isTrue){
          {{{{}}}}
        }"""
        out=str(Program([\
            FuncDecl(Id("foo"),[VarDecl(Id("arr"),ArrayPointerType(IntType())),\
            VarDecl(Id("iNum"),IntType()),\
            VarDecl(Id("isTrue"),BoolType())],IntType(),Block([Block([Block([Block([Block([])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,378))
    
    def test_81(self):
        inp="""int foo(int arr[], int iNum, boolean isTrue){
          {{{{iNum = iNum + 10;}}}}
        }"""
        out=str(Program([\
            FuncDecl(Id("foo"),[VarDecl(Id("arr"),ArrayPointerType(IntType())),\
                VarDecl(Id("iNum"),IntType()),\
                VarDecl(Id("isTrue"),BoolType())],IntType(),Block([\
                    Block([Block([Block([Block([BinaryOp("=",Id("iNum"),\
                    BinaryOp("+",Id("iNum"),IntLiteral(10)))])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,379))

    def test_88(self):
        inp="""int main(){
        int a, b, arr[10];
        boolean isTrue, isFact;
        string str;
        foo(2)[foo(2)[foo(2)]] = compare(a,b)[arr[foo(2)[15]]];
        foo(arr, arr)[compare(a,b)[25]+ compare(b,a)[29]] = foo(a,b,c,arrp[1])[2];
      }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),\
                VarDecl(Id("b"),IntType()),\
                VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),\
                VarDecl(Id("isTrue"),BoolType()),VarDecl(Id("isFact"),BoolType()),\
                VarDecl(Id("str"),StringType()),\
                BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),\
                ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),\
                CallExpr(Id("foo"),[IntLiteral(2)]))),\
                ArrayCell(CallExpr(Id("compare"),[Id("a"),Id("b")]),\
                ArrayCell(Id("arr"),ArrayCell(CallExpr(Id("foo"),\
                [IntLiteral(2)]),IntLiteral(15))))),BinaryOp("=",\
                ArrayCell(CallExpr(Id("foo"),[Id("arr"),Id("arr")]),\
                BinaryOp("+",ArrayCell(CallExpr(Id("compare"),[Id("a"),Id("b")]),\
                IntLiteral(25)),ArrayCell(CallExpr(Id("compare"),[Id("b"),Id("a")]),\
                IntLiteral(29)))),ArrayCell(CallExpr(Id("foo"),[Id("a"),Id("b"),Id("c"),\
                ArrayCell(Id("arrp"),IntLiteral(1))]),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,380))

    def test_89(self):
        inp="""int main(){
        int a, b, arr[10];
        boolean isTrue, isFact;
        string str;
        fact(a,10);
        foo(str, isTrue);
        compare(a,b,isTrue);
        getChar(str, isFact);
      }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([\
                VarDecl(Id("a"),IntType()),\
                VarDecl(Id("b"),IntType()),\
                VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),\
                VarDecl(Id("isTrue"),BoolType()),\
                VarDecl(Id("isFact"),BoolType()),\
                VarDecl(Id("str"),StringType()),\
                CallExpr(Id("fact"),[Id("a"),IntLiteral(10)]),\
                CallExpr(Id("foo"),[Id("str"),Id("isTrue")]),\
                CallExpr(Id("compare"),[Id("a"),Id("b"),Id("isTrue")]),\
                CallExpr(Id("getChar"),[Id("str"),Id("isFact")])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,381))

    def test_90(self):
        inp="""int main(){
        int a, b, arr[10];
        boolean isTrue, isFact;
        string str;
        fact(foo(2) + a + b,10);
        foo(str, a + 10 + b * 15);
        compare(a,a + 10 + b * 15,isTrue);
        getChar(str, a + 10 + b * 15);
      }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([\
            VarDecl(Id("a"),IntType()),\
            VarDecl(Id("b"),IntType()),\
            VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),\
            VarDecl(Id("isTrue"),BoolType()),\
            VarDecl(Id("isFact"),BoolType()),\
            VarDecl(Id("str"),StringType()),CallExpr(Id("fact"),\
            [BinaryOp("+",BinaryOp("+",CallExpr(Id("foo"),\
            [IntLiteral(2)]),Id("a")),Id("b")),IntLiteral(10)]),\
            CallExpr(Id("foo"),[Id("str"),BinaryOp("+",\
            BinaryOp("+",Id("a"),IntLiteral(10)),\
            BinaryOp("*",Id("b"),IntLiteral(15)))]),\
            CallExpr(Id("compare"),[Id("a"),BinaryOp("+",\
            BinaryOp("+",Id("a"),IntLiteral(10)),\
            BinaryOp("*",Id("b"),IntLiteral(15))),Id("isTrue")]),\
            CallExpr(Id("getChar"),[Id("str"),BinaryOp("+",\
            BinaryOp("+",Id("a"),IntLiteral(10)),\
            BinaryOp("*",Id("b"),IntLiteral(15)))])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,382))

    def test_91(self):
        inp="""int main(){
        int a, b, arr[10];
        boolean isTrue, isFact;
        string str;
        fact(foo(2)[10] + a + b,10[10]);
        foo(str[10], a + 10 + b[0] * 15);
        compare(a[3],a + 10 + b[2] * 15,isTrue);
        getChar(str[10], a + 10 + b[15] * 15);
      }"""
        out=str(Program([\
        FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("a"),IntType()),\
        VarDecl(Id("b"),IntType()),VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),\
        VarDecl(Id("isTrue"),BoolType()),VarDecl(Id("isFact"),BoolType()),\
        VarDecl(Id("str"),StringType()),\
        CallExpr(Id("fact"),[BinaryOp("+",BinaryOp("+",ArrayCell(\
        CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(10)),Id("a")),Id("b")),\
        ArrayCell(IntLiteral(10),IntLiteral(10))]),CallExpr(Id("foo"),[\
        ArrayCell(Id("str"),IntLiteral(10)),BinaryOp("+",\
        BinaryOp("+",Id("a"),IntLiteral(10)),BinaryOp("*",ArrayCell(Id("b"),\
        IntLiteral(0)),IntLiteral(15)))]),CallExpr(Id("compare"),[\
        ArrayCell(Id("a"),IntLiteral(3)),BinaryOp("+",BinaryOp("+",Id("a"),\
        IntLiteral(10)),BinaryOp("*",ArrayCell(Id("b"),IntLiteral(2)),\
        IntLiteral(15))),Id("isTrue")]),CallExpr(Id("getChar"),[ArrayCell(Id("str"),\
        IntLiteral(10)),BinaryOp("+",BinaryOp("+",Id("a"),IntLiteral(10)),\
        BinaryOp("*",ArrayCell(Id("b"),IntLiteral(15)),IntLiteral(15)))])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,383))

    def test_VarFunc_Decl_07(self):
        inp="""int iNum, max_level[5];
        string str,arr;
        boolean isTrue, isFact[5];
        void main(int iNum[]){}
        int foo(int number[]){}"""
        out=str(Program([\
            VarDecl(Id("iNum"),IntType()),\
            VarDecl(Id("max_level"),ArrayType(IntLiteral(5),IntType())),\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("arr"),StringType()),\
            VarDecl(Id("isTrue"),BoolType()),\
            VarDecl(Id("isFact"),ArrayType(IntLiteral(5),BoolType())),\
            FuncDecl(Id("main"),[VarDecl(Id("iNum"),ArrayPointerType(IntType()))],VoidType(),Block([])),\
            FuncDecl(Id("foo"),[VarDecl(Id("number"),ArrayPointerType(IntType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,384))   

    def test_VarFunc_Decl_08(self):
        inp="""int iNum, max_level[5];
        string str,arr;
        boolean isTrue, isFact[5];
        void main(int iNum, int size){}
        int foo(int number, int size){}"""
        out=str(Program([\
            VarDecl(Id("iNum"),IntType()),\
            VarDecl(Id("max_level"),ArrayType(IntLiteral(5),IntType())),\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("arr"),StringType()),\
            VarDecl(Id("isTrue"),BoolType()),\
            VarDecl(Id("isFact"),ArrayType(IntLiteral(5),BoolType())),\
            FuncDecl(Id("main"),[VarDecl(Id("iNum"),IntType()),VarDecl(Id("size"),IntType())],VoidType(),Block([])),\
            FuncDecl(Id("foo"),[VarDecl(Id("number"),IntType()),VarDecl(Id("size"),IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,385)) 

    def test_VarFunc_Decl_12(self):
        inp="""int iNum, max_level[5];
        string str,arr;
        boolean isTrue, isFact[5];
        void main(int iNum){}
        int[] foo(int number[]){}
        int[] maxst(int a){}
        boolean isFalse;
        int fNumber;
        int getFloat(float fNumber){}"""
        out=str(Program([\
            VarDecl(Id("iNum"),IntType()),\
            VarDecl(Id("max_level"),ArrayType(IntLiteral(5),IntType())),\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("arr"),StringType()),\
            VarDecl(Id("isTrue"),BoolType()),\
            VarDecl(Id("isFact"),ArrayType(IntLiteral(5),BoolType())),\
            FuncDecl(Id("main"),[VarDecl(Id("iNum"),IntType())],VoidType(),Block([])),\
            FuncDecl(Id("foo"),[VarDecl(Id("number"),ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([])),\
            FuncDecl(Id("maxst"),[VarDecl(Id("a"),IntType())],ArrayPointerType(IntType()),Block([])),\
            VarDecl(Id("isFalse"),BoolType()),\
            VarDecl(Id("fNumber"),IntType()),\
            FuncDecl(Id("getFloat"),[VarDecl(Id("fNumber"),FloatType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,386))  

    def test_VarFunc_Decl_13(self):
        inp="""int iNum, max_level[5];
        string str,arr;
        boolean isTrue, isFact[5];
        void main(int iNum){}
        int[] foo(int number[], int c, int d){}
        int[] maxst(int a, int Number){}
        boolean isFalse;
        int fNumber;
        int getFloat(float fNumber, boolean isFact[]){}
      """
        out=str(Program([\
            VarDecl(Id("iNum"),IntType()),\
            VarDecl(Id("max_level"),ArrayType(IntLiteral(5),IntType())),\
            VarDecl(Id("str"),StringType()),\
            VarDecl(Id("arr"),StringType()),\
            VarDecl(Id("isTrue"),BoolType()),\
            VarDecl(Id("isFact"),ArrayType(IntLiteral(5),BoolType())),\
            FuncDecl(Id("main"),[VarDecl(Id("iNum"),IntType())],VoidType(),Block([])),\
            FuncDecl(Id("foo"),[VarDecl(Id("number"),ArrayPointerType(IntType())),VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType())],ArrayPointerType(IntType()),Block([])),\
            FuncDecl(Id("maxst"),[VarDecl(Id("a"),IntType()),VarDecl(Id("Number"),IntType())],ArrayPointerType(IntType()),Block([])),VarDecl(Id("isFalse"),BoolType()),VarDecl(Id("fNumber"),IntType()),\
            FuncDecl(Id("getFloat"),[VarDecl(Id("fNumber"),FloatType()),VarDecl(Id("isFact"),ArrayPointerType(BoolType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,387))

    def test_VarFunc_Decl_14(self):
        inp="""int main(){
        int iNum;
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("iNum"),IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,388))   
        
    def test_VarFunc_Decl_15(self):
        inp="""int main(){
        int iNum, size, length;
        }"""
        out=str(Program([\
            FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("iNum"),IntType()),VarDecl(Id("size"),IntType()),VarDecl(Id("length"),IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,389))

    def test_Complex_12(self):
        inp=""" int compareString(string str1, string str2){
      int result;
      if (strlen(str1) >= strlen(str2)){
        for (i = 0; i < strlen(str2); i)
          result =abs(str1[i] - str2[i]);
        for (i = strlen(str2); i < strlen(str1); i)
          result =str1[i];
      }
      else{
        for(i=0;i<strlen(str1);i)
          for (i = strlen(str1); i < strlen(str2); i)
            result = str2[i];
      }
      return result;
     }"""
        out=str(Program([FuncDecl(Id("compareString"),[VarDecl(Id("str1"),StringType()),VarDecl(Id("str2"),StringType())],IntType(),\
            Block([VarDecl(Id("result"),IntType()),If(BinaryOp(">=",CallExpr(Id("strlen"),[Id("str1")]),CallExpr(Id("strlen"),[Id("str2")])),\
                Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),CallExpr(Id("strlen"),[Id("str2")])),Id("i"),BinaryOp("=",Id("result"),CallExpr(Id("abs"),[BinaryOp("-",ArrayCell(Id("str1"),Id("i")),ArrayCell(Id("str2"),Id("i")))]))),For(BinaryOp("=",Id("i"),CallExpr(Id("strlen"),[Id("str2")])),BinaryOp("<",Id("i"),CallExpr(Id("strlen"),[Id("str1")])),Id("i"),BinaryOp("=",Id("result"),ArrayCell(Id("str1"),Id("i"))))]),\
                Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),CallExpr(Id("strlen"),[Id("str1")])),Id("i"),For(BinaryOp("=",Id("i"),CallExpr(Id("strlen"),[Id("str1")])),BinaryOp("<",Id("i"),CallExpr(Id("strlen"),[Id("str2")])),Id("i"),BinaryOp("=",Id("result"),ArrayCell(Id("str2"),Id("i")))))])),Return(Id("result"))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,390))  

    def test_Complex_13(self):
        inp=""" void quickSort(int arr[], int left, int right) {
      int i,j;
      int tmp;
      int pivot; 
      i = left;
      j = right;
      pivot = arr[(left + right) / 2];
      if((i > j)){
        continue;
      }
      do{
        if (i <= j) {
          tmp = arr[i];
          arr[i] = arr[j];
          arr[j] = tmp;
          i = i + 1;
          j = j - 1;
        }
      }while (i <= j);
      if (left < j)
            quickSort(arr, left, j);
      if (i < right)
            quickSort(arr, i, right);
     }"""
        out=str(Program([FuncDecl(Id("quickSort"),[VarDecl(Id("arr"),ArrayPointerType(IntType())),VarDecl(Id("left"),IntType()),VarDecl(Id("right"),IntType())],VoidType(),\
            Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),IntType()),VarDecl(Id("tmp"),IntType()),VarDecl(Id("pivot"),IntType()),BinaryOp("=",Id("i"),Id("left")),BinaryOp("=",Id("j"),Id("right")),BinaryOp("=",Id("pivot"),ArrayCell(Id("arr"),BinaryOp("/",BinaryOp("+",Id("left"),Id("right")),IntLiteral(2)))),If(BinaryOp(">",Id("i"),Id("j")),\
                Block([Continue()]),None),\
            Dowhile([Block([If(BinaryOp("<=",Id("i"),Id("j")),Block([BinaryOp("=",Id("tmp"),ArrayCell(Id("arr"),Id("i"))),BinaryOp("=",ArrayCell(Id("arr"),Id("i")),ArrayCell(Id("arr"),Id("j"))),BinaryOp("=",ArrayCell(Id("arr"),Id("j")),Id("tmp")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),BinaryOp("=",Id("j"),BinaryOp("-",Id("j"),IntLiteral(1)))]),None)])],BinaryOp("<=",Id("i"),Id("j"))),If(BinaryOp("<",Id("left"),Id("j")),CallExpr(Id("quickSort"),[Id("arr"),Id("left"),Id("j")]),None),If(BinaryOp("<",Id("i"),Id("right")),CallExpr(Id("quickSort"),[Id("arr"),Id("i"),Id("right")]),None)]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,391))

    def test_Complex_14(self):
        inp=""" int main(){
        int n, i, flag;
        flag = 0;

        printf("Enter a positive integer: ");
        scanf("%d",n);

        for(i=2; i<=n/2; i=i+1){
          if(n%i==0){
              flag=1;
              break;
          }
        }

        if (flag==0)
            printf("%d is a prime number.",n);
        else
            printf("%d is not a prime number.",n);
        
        return 0;
        }
        """
        out=str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("n"),IntType()),VarDecl(Id("i"),IntType()),VarDecl(Id("flag"),IntType()),BinaryOp("=",Id("flag"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Enter a positive integer: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<=",Id("i"),BinaryOp("/",Id("n"),IntLiteral(2))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),\
            Block([If(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(1)),Break()]),None)])),If(BinaryOp("==",Id("flag"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("%d is a prime number."),Id("n")]),CallExpr(Id("printf"),[StringLiteral("%d is not a prime number."),Id("n")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,392))

    def test_Complex_15(self):
        inp="""
        void towerOfHanoi(int n, string from_rod, string to_rod, string aux_rod){
          if (n == 1){
              printf("n Move disk 1 from rod %c to rod %c", from_rod, to_rod);
              return;
          }
          towerOfHanoi(n-1, from_rod, aux_rod, to_rod);
          printf("n Move disk %d from rod %c to rod %c", n, from_rod, to_rod);
          towerOfHanoi(n-1, aux_rod, to_rod, from_rod);
        }
        int main(){
            int n;
            n=4;
            towerOfHanoi(n, "A", "B", "C");
            return 0;
        }"""
        out=str(Program([FuncDecl(Id("towerOfHanoi"),[VarDecl(Id("n"),IntType()),VarDecl(Id("from_rod"),StringType()),VarDecl(Id("to_rod"),StringType()),VarDecl(Id("aux_rod"),StringType())],VoidType(),\
            Block([If(BinaryOp("==",Id("n"),IntLiteral(1)),Block([CallExpr(Id("printf"),[StringLiteral("n Move disk 1 from rod %c to rod %c"),Id("from_rod"),Id("to_rod")]),Return(None)]),None),CallExpr(Id("towerOfHanoi"),[BinaryOp("-",Id("n"),IntLiteral(1)),Id("from_rod"),Id("aux_rod"),Id("to_rod")]),CallExpr(Id("printf"),[StringLiteral("n Move disk %d from rod %c to rod %c"),Id("n"),Id("from_rod"),Id("to_rod")]),CallExpr(Id("towerOfHanoi"),[BinaryOp("-",Id("n"),IntLiteral(1)),Id("aux_rod"),Id("to_rod"),Id("from_rod")])])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl(Id("n"),IntType()),BinaryOp("=",Id("n"),IntLiteral(4)),CallExpr(Id("towerOfHanoi"),[Id("n"),StringLiteral("A"),StringLiteral("B"),StringLiteral("C")]),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,393))   

    def test_Complex_16(self):
        inp="""
        int[] bouble(int array[], int n){
          int i, j, swap;
          for(i=0; i<n-1; i=i+1){
            for (j=0; j<n-i-1; j=j+1){
              if (array[j]>array[j+1]){
                swap=array[j];
                array[j]=array[j+1];
                array[j+1]=swap;
              }
            }
          }
        }"""
        out=str(Program([FuncDecl(Id("bouble"),[VarDecl(Id("array"),ArrayPointerType(IntType())),VarDecl(Id("n"),IntType())],ArrayPointerType(IntType()),\
            Block([VarDecl(Id("i"),IntType()),VarDecl(Id("j"),IntType()),VarDecl(Id("swap"),IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),\
                Block([For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),BinaryOp("-",BinaryOp("-",Id("n"),Id("i")),IntLiteral(1))),BinaryOp("=",Id("j"),BinaryOp("+",Id("j"),IntLiteral(1))),Block([If(BinaryOp(">",ArrayCell(Id("array"),Id("j")),ArrayCell(Id("array"),BinaryOp("+",Id("j"),IntLiteral(1)))),Block([BinaryOp("=",Id("swap"),ArrayCell(Id("array"),Id("j"))),BinaryOp("=",ArrayCell(Id("array"),Id("j")),ArrayCell(Id("array"),BinaryOp("+",Id("j"),IntLiteral(1)))),BinaryOp("=",ArrayCell(Id("array"),BinaryOp("+",Id("j"),IntLiteral(1))),Id("swap"))]),None)]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,394))   

    def test_Complex_17(self):
        inp="""int main(){
        int a, b, arr[10];
        boolean isTrue, isFact;
        string str;
        (arr[0])[10] = arr[5]*2;
        foo(2)[10] = foo(2) + a + b;
      }"""
        out=str(Program([FuncDecl(Id("main"),[],IntType(),\
            Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),VarDecl(Id("isTrue"),BoolType()),VarDecl(Id("isFact"),BoolType()),VarDecl(Id("str"),StringType()),BinaryOp("=",ArrayCell(ArrayCell(Id("arr"),IntLiteral(0)),IntLiteral(10)),BinaryOp("*",ArrayCell(Id("arr"),IntLiteral(5)),IntLiteral(2))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(10)),BinaryOp("+",BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(2)]),Id("a")),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,395))  

    def test_Complex_18(self):
        inp="""int main(){
        int a, b, arr[10];
        boolean isTrue, isFact;
        string str;
        foo(2)[foo(2)[foo(2)]] = compare(a,b)[arr[foo(2)[15]]];
        foo(arr, arr)[compare(a,b)[25]+ compare(b,a)[29]] = foo(a,b,c,arrp[1])[2];
      }"""
        out=str(Program([FuncDecl(Id("main"),[],IntType(),\
            Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),VarDecl(Id("isTrue"),BoolType()),VarDecl(Id("isFact"),BoolType()),VarDecl(Id("str"),StringType()),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),CallExpr(Id("foo"),[IntLiteral(2)]))),ArrayCell(CallExpr(Id("compare"),[Id("a"),Id("b")]),ArrayCell(Id("arr"),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(15))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[Id("arr"),Id("arr")]),BinaryOp("+",ArrayCell(CallExpr(Id("compare"),[Id("a"),Id("b")]),IntLiteral(25)),ArrayCell(CallExpr(Id("compare"),[Id("b"),Id("a")]),IntLiteral(29)))),ArrayCell(CallExpr(Id("foo"),[Id("a"),Id("b"),Id("c"),ArrayCell(Id("arrp"),IntLiteral(1))]),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,396))  

    def test_Complex_19(self):
        inp="""int main(){
        int a, b, arr[10];
        boolean isTrue, isFact;
        string str;
        fact(a,10);
        foo(str, isTrue);
        compare(a,b,isTrue);
        getChar(str, isFact);
      }"""
        out=str(Program([FuncDecl(Id("main"),[],IntType(),\
            Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),VarDecl(Id("isTrue"),BoolType()),VarDecl(Id("isFact"),BoolType()),VarDecl(Id("str"),StringType()),CallExpr(Id("fact"),[Id("a"),IntLiteral(10)]),CallExpr(Id("foo"),[Id("str"),Id("isTrue")]),CallExpr(Id("compare"),[Id("a"),Id("b"),Id("isTrue")]),CallExpr(Id("getChar"),[Id("str"),Id("isFact")])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,397))   

    def test_Complex_20(self):
        inp="""int main(){
        int a, b, arr[10];
        boolean isTrue, isFact;
        string str;
        fact(foo(2) + a + b,10);
        foo(str, a + 10 + b * 15);
        compare(a,a + 10 + b * 15,isTrue);
        getChar(str, a + 10 + b * 15);
      }"""
        out=str(Program([FuncDecl(Id("main"),[],IntType(),\
            Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),VarDecl(Id("isTrue"),BoolType()),VarDecl(Id("isFact"),BoolType()),VarDecl(Id("str"),StringType()),CallExpr(Id("fact"),[BinaryOp("+",BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(2)]),Id("a")),Id("b")),IntLiteral(10)]),CallExpr(Id("foo"),[Id("str"),BinaryOp("+",BinaryOp("+",Id("a"),IntLiteral(10)),BinaryOp("*",Id("b"),IntLiteral(15)))]),CallExpr(Id("compare"),[Id("a"),BinaryOp("+",BinaryOp("+",Id("a"),IntLiteral(10)),BinaryOp("*",Id("b"),IntLiteral(15))),Id("isTrue")]),CallExpr(Id("getChar"),[Id("str"),BinaryOp("+",BinaryOp("+",Id("a"),IntLiteral(10)),BinaryOp("*",Id("b"),IntLiteral(15)))])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,398))   

    def test_Complex_21(self):
        inp="""int main(){
        int a, b, arr[10];
        boolean isTrue, isFact;
        string str;
        fact(foo(2)[10] + a + b,10[10]);
        foo(str[10], a + 10 + b[0] * 15);
        compare(a[3],a + 10 + b[2] * 15,isTrue);
        getChar(str[10], a + 10 + b[15] * 15);
      }"""
        out=str(Program([FuncDecl(Id("main"),[],IntType(),\
            Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("arr"),ArrayType(IntLiteral(10),IntType())),VarDecl(Id("isTrue"),BoolType()),VarDecl(Id("isFact"),BoolType()),VarDecl(Id("str"),StringType()),CallExpr(Id("fact"),[BinaryOp("+",BinaryOp("+",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),IntLiteral(10)),Id("a")),Id("b")),ArrayCell(IntLiteral(10),IntLiteral(10))]),CallExpr(Id("foo"),[ArrayCell(Id("str"),IntLiteral(10)),BinaryOp("+",BinaryOp("+",Id("a"),IntLiteral(10)),BinaryOp("*",ArrayCell(Id("b"),IntLiteral(0)),IntLiteral(15)))]),CallExpr(Id("compare"),[ArrayCell(Id("a"),IntLiteral(3)),BinaryOp("+",BinaryOp("+",Id("a"),IntLiteral(10)),BinaryOp("*",ArrayCell(Id("b"),IntLiteral(2)),IntLiteral(15))),Id("isTrue")]),CallExpr(Id("getChar"),[ArrayCell(Id("str"),IntLiteral(10)),BinaryOp("+",BinaryOp("+",Id("a"),IntLiteral(10)),BinaryOp("*",ArrayCell(Id("b"),IntLiteral(15)),IntLiteral(15)))])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,398))  

    def test_Complex_22(self):
        inp="""int MAX_SIZE;
      int sum;
      void swap(int a, int b){
        int c;
        c = a;
        a = b;
        b = c;  
      }
      int main(){
        int a, b;
        swap(a,b);
        println(a,b);
      }"""
        out=str(Program([VarDecl(Id("MAX_SIZE"),IntType()),VarDecl(Id("sum"),IntType()),FuncDecl(Id("swap"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],VoidType(),\
            Block([VarDecl(Id("c"),IntType()),BinaryOp("=",Id("c"),Id("a")),BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("c"))])),FuncDecl(Id("main"),[],IntType(),\
            Block([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),CallExpr(Id("swap"),[Id("a"),Id("b")]),CallExpr(Id("println"),[Id("a"),Id("b")])]))]))
        self.assertTrue(TestAST.checkASTGen(inp,out,399))   
    