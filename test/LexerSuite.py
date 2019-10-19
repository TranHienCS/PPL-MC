import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_underscore_id(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("143.e5","143.,e5,<EOF>",101))
    def test_low_up_id(self):       
        self.assertTrue(TestLexer.checkLexeme("_aBc","_aBc,<EOF>",102))
    def test_digit_id(self):       
        self.assertTrue(TestLexer.checkLexeme("_A12_b","_A12_b,<EOF>",103))            
    
    def test_boolean_keyword(self):       
        self.assertTrue(TestLexer.checkLexeme("boolean a","boolean,a,<EOF>",104))
        """test Comment"""    
    def test_comment_1(self):       
        self.assertTrue(TestLexer.checkLexeme("//boolean a 1.2e5","<EOF>",105))
    def test_comment_2(self):       
        self.assertTrue(TestLexer.checkLexeme("/*boolean a 1.2e5*/","<EOF>",106))
    def test_comment_3(self): 
        input = "// abc \n 345"
        expect = "345,<EOF>"    
        self.assertTrue(TestLexer.checkLexeme(input,expect,107))
        """test String"""

    def test_string_1(self): 
        input = """ "nguyentrongdu" """
        expect = "nguyentrongdu,<EOF>"    
        self.assertTrue(TestLexer.checkLexeme(input,expect,108))
    def test_string_2(self): 
        input = """ "nguyentrongdu\\n" """
        expect = "nguyentrongdu\\n,<EOF>"    
        self.assertTrue(TestLexer.checkLexeme(input,expect,109))
    def test_string_3(self): 
        input = """  "nguyen\btrong\tdu\f" 
                """
        expect = "nguyen\btrong\tdu\f,<EOF>"              
        self.assertTrue(TestLexer.checkLexeme(input,expect,110))
    def test_string_4(self):
        input = """ "boolean int float void string" """
        expect = "boolean int float void string,<EOF>" 
    def test_string_5(self): 
        input = """ "" """
        expect = """,<EOF>"""    
        self.assertTrue(TestLexer.checkLexeme(input,expect,111))
    def test_string_6(self): 
        input = """ "\\'" """
        expect = """\\',<EOF>"""   
        self.assertTrue(TestLexer.checkLexeme(input,expect,112))
    def test_string_7(self): 
        input = """ "\\n" """
        expect = """\\n,<EOF>"""   
        self.assertTrue(TestLexer.checkLexeme(input,expect,113))
    def test_string_8(self): 
        input = """ " """
        expect = """Unclosed String:  """   
    def test_string_9(self): 
        input = """ "du\\ """
        expect = """Illegal Escape In String: du\\ """
    def test_string_10(self): 
        input = """putString("This is String?)"""
        expect = """putString,(,Unclosed String: This is String?)"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,114))
    def test_string_11(self): 
        input = """ "nguyentrongdu/**/" """
        expect = "nguyentrongdu/**/,<EOF>"    
        self.assertTrue(TestLexer.checkLexeme(input,expect,115))
    def test_string_12(self): 
        input = """ "nguyentrongdu\\\\pvl" """
        expect = "nguyentrongdu\\\\pvl,<EOF>"    
        self.assertTrue(TestLexer.checkLexeme(input,expect,116))
    def test_string_13(self): 
        input = """ "nguyentrongdu\\pvl" """
        expect = "Illegal Escape In String: nguyentrongdu\\p"    
    def test_string_14(self): 
        input = """ "\\z" """
        expect = "Illegal Escape In String: \\z"
        self.assertTrue(TestLexer.checkLexeme(input,expect,117))
    def test_string_15(self):
        input = """ "\____" """
        expect = "Illegal Escape In String: \_"
        self.assertTrue(TestLexer.checkLexeme(input,expect,118))
    def test_string_16(self): 
        input = """ ABCD int float""abc """
        expect = "ABCD,int,float,,abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,119))
        """test floating-point literal"""
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("1.2","1.2,<EOF>",120))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("1.","1.,<EOF>",121))
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme(".1",".1,<EOF>",122))
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("1e2","1e2,<EOF>",123))
    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme("1.2E-2","1.2E-2,<EOF>",124))
    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme("1.2e-2","1.2e-2,<EOF>",125))
    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme(".1E2",".1E2,<EOF>",126))
    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme("9.0","9.0,<EOF>",127))
    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme("12e8","12e8,<EOF>",128))
    def test_float_10(self):
        self.assertTrue(TestLexer.checkLexeme("0.33E-3","0.33E-3,<EOF>",129))
    def test_float_11(self):
        self.assertTrue(TestLexer.checkLexeme("128e-42","128e-42,<EOF>",130))
    def test_float_12(self):
        input = "11.2 11. .21 15e2"
        expect = "11.2,11.,.21,15e2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,131))
    def test_float_13(self):
        input = "78.2E-2 234.2e-2 .155E2 9.10"
        expect = "78.2E-2,234.2e-2,.155E2,9.10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,132))
    def test_float_14(self):
        input = "12e87 0.433E-34 1428e-442"
        expect = "12e87,0.433E-34,1428e-442,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,133))
    def test_float_15(self):
        input = "12e8704.433E-341428e-442"
        expect = "12e8704,.433E-341428,e,-,442,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,134))
    def test_float_16(self):
        input = "12e8704.433E+341428e-+442"
        expect = "12e8704,.433,E,+,341428,e,-,+,442,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,135))
    def test_float_17(self):
        input = "12e-87+04.43-3E-341+428e-44-2"
        expect = "12e-87,+,04.43,-,3E-341,+,428e-44,-,2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,136))
    def test_float_18(self):
        input = "143+143.0+143e5+143e-5+143.e5+143.15e5"
        expect = "143,+,143.0,+,143e5,+,143e-5,+,143.,e5,+,143.15e5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,137))
        """test integers"""
    def test_integer_1(self):      
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",138))
    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("123_","123,_,<EOF>",139))
    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("123_123","123,_123,<EOF>",140))
    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("1","1,<EOF>",141))
    def test_integer_5(self):
        self.assertTrue(TestLexer.checkLexeme("_123","_123,<EOF>",142))
    def test_integer_6(self):
        self.assertTrue(TestLexer.checkLexeme("123_a123","123,_a123,<EOF>",143))
        '''test operator'''
    def test_operator_1(self):
        self.assertTrue(TestLexer.checkLexeme("a=10","a,=,10,<EOF>",144))
    def test_operator_2(self):
        self.assertTrue(TestLexer.checkLexeme("a>10","a,>,10,<EOF>",145))
    def test_operator_3(self):
        self.assertTrue(TestLexer.checkLexeme("a>=b","a,>=,b,<EOF>",146))
    def test_operator_4(self):
        self.assertTrue(TestLexer.checkLexeme("a<b+c","a,<,b,+,c,<EOF>",147))
    def test_operator_5(self):
        self.assertTrue(TestLexer.checkLexeme("a+b<=a-c","a,+,b,<=,a,-,c,<EOF>",148))
    def test_operator_6(self):
        self.assertTrue(TestLexer.checkLexeme("a mod b=2","a,mod,b,=,2,<EOF>",149))
    def test_operator_7(self):
        self.assertTrue(TestLexer.checkLexeme("a div 2=0","a,div,2,=,0,<EOF>",150))
    def test_operator_8(self):
        self.assertTrue(TestLexer.checkLexeme("a*b-c+d/e","a,*,b,-,c,+,d,/,e,<EOF>",151))
    def test_operator_9(self):
        self.assertTrue(TestLexer.checkLexeme("======","==,==,==,<EOF>",152))
    def test_operator_10(self):
        self.assertTrue(TestLexer.checkLexeme("""!==!====!=====!==""","!=,=,!=,==,=,!=,==,==,!=,=,<EOF>",153))
    def test_operator_11(self):
        self.assertTrue(TestLexer.checkLexeme("""!a!a!a!a!a=!=!=aaa!<><>""","!,a,!,a,!,a,!,a,!,a,=,!=,!=,aaa,!,<,>,<,>,<EOF>",154))
        '''test uncloseString'''
    def test_uncloseString_1(self):
        self.assertTrue(TestLexer.checkLexeme(" \"\\\" " ,"""Unclosed String: \\" """,155))
    def test_uncloseString_2(self):
        self.assertTrue(TestLexer.checkLexeme(" \"avcdq","""Unclosed String: avcdq""",156))
    def test_uncloseString_3(self):
        self.assertTrue(TestLexer.checkLexeme(" \"a@@#$$%% ","""Unclosed String: a@@#$$%% """,157))
    def test_uncloseString_4(self):
        self.assertTrue(TestLexer.checkLexeme(" \"abcd\" \"xyz ","""abcd,Unclosed String: xyz """,158))
    def test_uncloseString_5(self):
        self.assertTrue(TestLexer.checkLexeme(" \"\"\" ",""",Unclosed String:  """,159))
        '''test illegalEscape'''
    def test_illegalEscape_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "aa\\kbb" ""","""Illegal Escape In String: aa\\k""",160))
    def test_illegalEscape_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "akdkkk\\\\\\kadadad" ""","""Illegal Escape In String: akdkkk\\\\\\k""",161))
    def test_illegalEscape_3(self):
        self.assertTrue(TestLexer.checkLexeme(" \"\\ ","Illegal Escape In String: \\ ",162))
    def test_illegalEscape_4(self):
        self.assertTrue(TestLexer.checkLexeme(" \"\\t\\ ","Illegal Escape In String: \\t\\ ",163))
    def test_illegalEscape_5(self):
        self.assertTrue(TestLexer.checkLexeme(" \"\\k\\\\ ","Illegal Escape In String: \\k",164))
        '''test pointer'''
    def test_pointer_1(self):
        self.assertTrue(TestLexer.checkLexeme("int[] hien(string a[])","int,[,],hien,(,string,a,[,],),<EOF>",165))
    def test_pointer_2(self):
        self.assertTrue(TestLexer.checkLexeme("float[] foo(){}","float,[,],foo,(,),{,},<EOF>",166))
        
    def test_whole_1(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,167))
    def test_whole_2(self):
        input = "main int {"
        expect = "main,int,{,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,168))
    def test_whole_3(self):
        input = "" "aaaa" ""
        expect = "aaaa,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,169))
    def test_whole_4(self):
        input = "\"aaaa"
        expect = "Unclosed String: aaaa"
        self.assertTrue(TestLexer.checkLexeme(input,expect,170))
    def test_whole_5(self):
        input = "} int main {"
        expect = "},int,main,{,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,171))
    def test_whole_6(self):
        input = "void main (){}"
        expect = "void,main,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,172))
    def test_whole_7(self):
        input = "void main (){ a = 1 ;}"
        expect = "void,main,(,),{,a,=,1,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,173))
    def test_whole_8(self):
        input = "void foo(int i){}"
        expect = "void,foo,(,int,i,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,174))
    def test_whole_9(self):
        input = "for(int i = 1; i <= rows; i=i+2)"
        expect = "for,(,int,i,=,1,;,i,<=,rows,;,i,=,i,+,2,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,175))
    def test_whole_10(self):
        input = "void foo(int i){}"
        expect = "void,foo,(,int,i,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,176))
    def test_whole_11(self):
        input = "int main (){putIntLn(4);}"
        expect = "int,main,(,),{,putIntLn,(,4,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,177))
    def test_whole_12(self):
        input = "int_float"
        expect = "int_float,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,178))
    def test_whole_13(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,179))
    def test_whole_14(self):
        input = "abc#"
        expect = "abc,Error Token #"
        self.assertTrue(TestLexer.checkLexeme(input,expect,180))
    def test_whole_15(self):
        input = "?#"
        expect = "Error Token ?"
        self.assertTrue(TestLexer.checkLexeme(input,expect,181))
    def test_whole_16(self):
        input = "`abc"
        expect = "Error Token `"
        self.assertTrue(TestLexer.checkLexeme(input,expect,182))
    def test_whole_17(self):
        input = "$abc"
        expect = "Error Token $"
        self.assertTrue(TestLexer.checkLexeme(input,expect,183))
    def test_whole_18(self):
        input = "&abc"
        expect = "Error Token &"
        self.assertTrue(TestLexer.checkLexeme(input,expect,184))
    def test_whole_19(self):
        input = "|abc"
        expect = "Error Token |"
        self.assertTrue(TestLexer.checkLexeme(input,expect,185))
    def test_whole_20(self):
        input ="""int checkPrimeNumber(int n)
             {
                for(i=2; i<=n/2; i=i+1)
                {
                /* condition for non-prime number */
                    if(n%i == 0)
                    {
                        flag = 0;
                        break;
                    }
                }
             }"""
        expect ="""int,checkPrimeNumber,(,int,n,),{,for,(,i,=,2,;,i,<=,n,/,2,;,i,=,i,+,1,),{,if,(,n,%,i,==,0,),{,flag,=,0,;,break,;,},},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,186))
    def test_whole_21(self):
        input ="""int main() {
                int gd = DETECT, gm;
                /* initialization
                of graphic mode */
                initgraph(&gd, &gm, "C:\\TC\\BGI");
                line(100,100,200, 200);
                getch();
                closegraph();
                return 0;
             }"""
        expect ="""int,main,(,),{,int,gd,=,DETECT,,,gm,;,initgraph,(,Error Token &"""        
        self.assertTrue(TestLexer.checkLexeme(input,expect,187))

    def test_whole_22(self):
        input ="""// ham tinh so mu
             int power(int, int);
             void main(void)
             {
             printf("2 mu 2 = %d.", power(2, 2));
             printf("2 mu 3 = %d.", power(2, 3));
             }"""
        expect ="""int,power,(,int,,,int,),;,void,main,(,void,),{,printf,(,2 mu 2 = %d.,,,power,(,2,,,2,),),;,printf,(,2 mu 3 = %d.,,,power,(,2,,,3,),),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,188))
    def test_whole_23(self):
        input ="""void in_cuuchuong2(void)
             {
                        for(int i=1;i<=10;i=i+1)
                                     printf("2 x %d = %d", i, i*2);
             }"""
        expect ="""void,in_cuuchuong2,(,void,),{,for,(,int,i,=,1,;,i,<=,10,;,i,=,i,+,1,),printf,(,2 x %d = %d,,,i,,,i,*,2,),;,},<EOF>"""
       
        self.assertTrue(TestLexer.checkLexeme(input,expect,189))
    def test_whole_24(self):
        input ="""int main(void)
             {
                    {int z;
                     int y;
                     printf("nhap z:");
                     scanf("%d",z);
                     printf("nhap y:");
                     scanf("%d",y);
                     printf("%d + %d = %d", z, y,add(z, y));
                     printf ("gia tri tuyet doi cua %d la %d, y, abs(y));}}"""
        expect ="""int,main,(,void,),{,{,int,z,;,int,y,;,printf,(,nhap z:,),;,scanf,(,%d,,,z,),;,printf,(,nhap y:,),;,scanf,(,%d,,,y,),;,printf,(,%d + %d = %d,,,z,,,y,,,add,(,z,,,y,),),;,printf,(,Unclosed String: gia tri tuyet doi cua %d la %d, y, abs(y));}}"""
       
        self.assertTrue(TestLexer.checkLexeme(input,expect,190))
    def test_whole_25(self):
        input ="""|&$$$###########"""
        expect ="""Error Token |"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,191))
    def test_whole_26(self):
        input ="""&$$$###########"""
        expect ="""Error Token &"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,192))
    def test_whole_27(self):
        input ="""{}{}{}"""
        expect ="{,},{,},{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,193))
    def test_whole_28(self):
        input ="""{{(abc)}}"""
        expect ="{,{,(,abc,),},},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,194))
    def test_whole_29(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,195))
    def test_whole_30(self):
        input ="""if(true){a<=b && c>d}"""
        expect ="if,(,true,),{,a,<=,b,&&,c,>,d,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,196))
    def test_whole_31(self):
        input ="""foo(2)[3+x]=a[b[5]]+2;"""
        expect ="foo,(,2,),[,3,+,x,],=,a,[,b,[,5,],],+,2,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,197))
    def test_whole_32(self):
        input ="""=!<><>==<><>==<><>!="""
        expect ="=,!,<,>,<,>=,=,<,>,<,>=,=,<,>,<,>,!=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,198))
    def test_whole_33(self):
        input ="""!a!a!a!a!a=!=!=aaa!<><>"""
        expect ="!,a,!,a,!,a,!,a,!,a,=,!=,!=,aaa,!,<,>,<,>,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,199))
    def test_whole_34(self):
        input ="""(foo)(abc)(int)"""
        expect ="(,foo,),(,abc,),(,int,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,200))
