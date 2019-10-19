import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int abc[3];
            float a,b,c;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_more_complex_program1(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_simple_program1(self):
        input="""int abc[3];
            void main() {}"""
        expect= "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_simple_program2(self):
        input="""int variable1;
        void main() {}"""
        expect= "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_simple_program3(self):
        input="} int main {"
        expect="Error on line 1 col 0: }"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_simple_program4(self):
        input="""int var1,var2;
                    int main() """
        expect ="Error on line 2 col 31: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_simple_program5(self):
        input="""int var1,var2[];
                    int main(){} """
        expect ="Error on line 1 col 14: ]"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_simple_program6(self):
        input="""int var1,var2[3];
                    int main(){}"""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_simple_program7(self):
        input="""int var1,var2[3;
                    int main(){} """
        expect ="Error on line 1 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_simple_program8(self):
        input="int variable = 1;"
        expect="Error on line 1 col 13: ="
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_simple_program9(self):
        input="int abc, variable = 1;"
        expect="Error on line 1 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_simple_program10(self):
        input="""int func(){}
                void main(){}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_simple_program11(self):
        input="""int[] func(){}
                void main(){}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_simple_program12(self):
        input="void func( {}"
        expect="Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_simple_program13(self):
        input="void func()"
        expect="Error on line 1 col 11: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_simple_program14(self):
        input="""void main(int var1){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_simple_program15(self):
        input="""void main(int var1,float var2){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_simple_program16(self):
        input="""void main(int var1,float var2,string var3){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_simple_program17(self):
        input="""void main(int var1[]){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_simple_program18(self):
        input="""void main(int var1[],float var2[]){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_simple_program19(self):
        input="""void main(void a){}"""
        expect = "Error on line 1 col 10: void"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_simple_program20(self):
        input="""void[] func(boolean abc, float xyz) {
            int x1;
            float x2;
        }"""
        expect="Error on line 1 col 4: ["
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_simple_program21(self):
        input="""void func(boolean abc, float xyz) {
            int x1;
            float x2;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_simple_program22(self):
        input="""int[] func(boolean abc[], float xyz) {
            int x1;
            float x2;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_simple_program23(self):
        input="""void func() {
            break;
            }
            void main() {}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_simple_program24(self):
        input="""int func() {
            float abc;
            abc = 1;
            }
            void main() {}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_simple_program25(self):
        input="""int func(int par1, float par2){
                if (a != 1)
                    continue;
                else
                    break;
                return a;
                }
                void main() {}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_simple_program26(self):
        input="""int func(int par1, float par2){
                for(a = 10; a < 20; a = a + 1 )
                    i = i + 1;
                }
                void main() {}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_simple_program27(self):
        input="""int func(int par1, float par2){
                do a = 1; while a = 1;
                    continue;
                }
                void main() {}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_simple_program28(self):
        input="""int[] func(int var1, float var2[]){
                    do a = a+1; while a < 11;
                    return a = 1;
                }
                void main() {}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_simple_program29(self):
        input="""void foo1(int a){}
                void foo2(int b){}
                void foo3(int c){}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_simple_program30(self):
        input="""int func(int var, float i){
                abc = a[b[2]] + 3;
                    return a[3];
                }
                void main() {}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_simple_program31(self):
        input="""void main() {
                int abc;
                continue;
                putInt(i);
                }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_simple_program32(self):
        input="""int i,j,k[];
                void func(string a[],float f){
                    i =10;
                    return foo(2)[i+3];
                }"""
        expect="Error on line 1 col 10: ]"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_simple_program33(self):
        input="""int i,j,k[4];
                void func(string a[],float f){
                    i =10;
                    return foo(2)[i+3];
                }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_simple_program34(self):
        input="""int i,j,k[4];
                void func(string a[],float f){
                    i =10;
                    k[3]=func(x*2);
                    return foo(2)[i+3];
                }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_simple_program35(self):
        input="""int i[3];
                void func(string a[],float f){
                    func(i[4]*2);
                    return a[5];
                }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_wrong_program36(self):
        input="""int i[3];
                i[3]=3;
                void func(string a[],float f){
                }"""
        expect="Error on line 2 col 16: i"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_simple_program37(self):
        input="""int i[3];
                int func(string a[],float f){
                    int i,j,k[10];
                    g = (i+1)/(j+2)*5-k[4];
                    return g;
                }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_more_complex_program38(self):
        input="""boolean a;
                void func(boolean b){
                    b=false;
                    a=b;
                }
                void main(){
                    boolean x;
                    x=true;
                    func(x);
                    putBool(a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_ifstmt39(self):
        input="""void main(){
            if(a>b) a[3]=4;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_ifstmt40(self):
        input="""string[] func(boolean a){
            if(a==b) {
                a=1;
                b=2;
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_ifstmt41(self):
        input="""void main(){
            if(foo(2)[3]==a[b[4]]){
                putBool(true);
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_ifstmt42(self):
        input="""void main(){
            if(true)
                a=b;
            else
                b=a;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_ifstmt44(self):
        input="""void main(){
            if(true){
                    a=b;
                    c=d;
                }
            else
                b=a;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_ifstmt45(self):
        input="""void main(){
            if(true){
                if(a)
                    x=y;
                }
            else
                b=a;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_ifstmt46(self):
        input="""void main(){
            if(true){
                    if(false){
                        x=y;
                        a=b;
                    }
                    else b=b-1;
                }
            else
                {b=a;
                putInLn(10);
                }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_ifstmt47(self):
        input="""void main(){
            if(x!=3&&x / 2 ==0)
                if(x % 6==0||x/9=5)
                break;
                else continue;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_ifstmt48(self):
        input="""void main(){
            if(x!=3&&x / 2 ==0)
                if(x % 6==0||x/9==5)
                    break;
                else break;
            else return;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_whilestmt49(self):
        input="""void main(){
            int a,b[4],c;
            do x=x+2;
            while x<10;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_whilestmt50(self):
        input="""void main(){
            do x=x+2;
                getInt();
            while x<10;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_whilestmt51(self):
        input="""void main(){
            do x=x+2;
                getInt();
                if(x!=0) return true;
            while x<10;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_whilestmt52(self):
        input="""void main(){
            do  x=x+2;
                {
                    getInt();
                    if(x!=0) return true;
                }
                x=x%2;
            while (x<10&&x>6);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_whilestmt53(self):
        input="""void main(){
            do  x=x+2;
                {
                    getInt();
                    if(x!=0) return true;
                }
                {
                    if(x) break;
                }
                x=x%2;
            while (x<10&&x>6);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_whilestmt54(self):
        input="""void main(){
            do  x=x+2;
                do x=x*2;
                while(true);
            while (x<10&&x>6);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_forstmt55(self):
        input="""void main(){
            for(i=1;true;i=i+1)
                putInt(1);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_forstmt56(self):
        input="""void main(){
            for(a;b;c)
                putInt(1);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_forstmt57(self):
        input="""void main(){
            for(a;b;c)
                for(x;y;z){
                    do x();
                    while(x);
                }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_forstmt58(self):
        input="""void main(){
            for(a;b;c)
                for(x;y;z){
                    for(1;2;3){
                        getInt();
                    }
                }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_forstmt59(self):
        input="""void main(){
            for(i=1;i<10;i=i+2){
                swap(x,y);
                foo(3)[5]=func(3,i+1);
            }
        }
        void swap(int x,int y){
                x=y;
                y=x;
            }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_forstmt60(self):
        input="""void main(){
            for(i=1;i<10;i=i+2){
                for(j=1;j<20;j=j*2)
                    swap(x,y);
                foo(3)[5]=func(3,i+1);
            }
        }
        void swap(int x,int y){
                x=y;
                y=x;
            }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_breakstm61(self):
        input="""void main(){
            if(a>0) break;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_breakstm62(self):
        input="""int[] foo(int a[],float b){
            for(i=1;cond;stm){
                if(i>5) break;
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_breakstm63(self):
        input="""int[] foo(int a[],float b){
            for(i=1;cond;stm){
                do break;
                while false;
                break;
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_continuestm64(self):
        input="""void main(){
            for(i=0;i<n;i=i+1){
                if(i%2==0) break;
                else continue;
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_continuestm65(self):
        input="""void main(){
            for(i=0;i<n;i=i+1){
                if(i%2==0) continue;
                else continue;
                for(j=0;j<i;j=j-1){
                    continue;
                    {
                        continue;
                    }
                }
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_returnstm66(self):
        input="""void main(){
                x = foo(3)[10];
            }
            int[] foo(int a){
                int k;
                k= a*a;
                return a;
            }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_returnstm67(self):
        input="""int func(float b){
            return func(b+2);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_returnstm68(self):
        input="""int func(float b){
            return func(b+2)[x[2]+2];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_expresstionstm69(self):
        input="""int main(){
            int a,b[3],c;
            a=b;
            foo(a,b);
            100;
            c+2;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_expresstionstm70(self):
        input="""void main(){
            putString("abc\\n");
            func1(a,b[5])[6+x[3]];
        }"""
        expect= "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_expresstionstm71(self):
        input="""void main(){
            x+1;
            a % b;
        }"""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_blockstm72(self):
        input="""int func(int a[]){
            for(i=0;i<n;i=i+1){
                putInt(i);
                break;
            }
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_blockstm73(self):
        input="""void main(){
            {
                int a;
                float b;
                putFloat(a+b);
                {
                    int x;
                    int y;
                    putInt(x+y);
                }
            }
            
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_blockstm74(self):
        input="""int main(){
            do 
                i=getInt();
                {
                    for(i;i<n;i=i+1){
                        dosomething(i);
                        return 0;
                    }
                    break;
                }
                while(i<10);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_blockstm75(self):
        input="""
        string s,d,k[3];
        int main(){
            do {
                s=getString();
                putStringLn(s+d);
            }
            {
                int a,b,c;
                c=a+b;
                {
                    a=a+b;
                    putInt(a);
                }
            }
            while(true);
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_index_expression76(self):
        input="""int i,j,k[3];
            void main(){
                k[foo[3]]=3;
                foo(3)[i+1]=k[3];
            }
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_index_expression77(self):
        input="""int x,y,z[100];
            int[] func(int a[],int b[]){
                z[x[3]+y[5]] = foo(x[3+x])[10+x];
            }
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_index_expression78(self):
        input="""int x,y,z[100];
            int[] func(int a[],int b[]){
                z[x[3]+y[5]] = foo(x[3+x])[10+x];
                m= a[b[3]];
                boolean b;
            }
        """
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_whole_79(self):
        input = """float foo(float x, float y){
                    x;
                    foo(x+y);
                    y;
                  }
                  boolean check(){
                    if(a>x)
                      return a;
                    else
                      if (a != 1)
                        for(a = 10; a < 20; a = a + 1 )
                            i = i + 1;
                      else
                        foo(x+y);
                    y;
                  }
                  void main() {
                  int abc;
                  int x,y;
                  for( abc = 1; xyz == true; abc = abc + 1)
                      if(abc == 1)
                        abc = 0;
                      else
                        do abc = abc + 1;
                        while xyz != false;
                  return 0;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_whole_80(self):
        input = """void foo(){
            int i, k[1]; float j[10];
            i = k[j[10]];
            xyz = false;
            if(bl = false)
              xyz = true;
            else
              xyz = false;
            return 0;
        }
        int func(int par1, float par2){
            if (a != 1)
              continue;
            else
              break;
        }
                void main(){
                do a = 1;
                while arr[arr[2]] == arr[arr[3]];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_whole_81(self):
        input = """void foo(){
            int i, k[1]; float j[10];
            i = k[j[10]];
        }
        void foo ( int i ) {
            int i,j,k[5];
            i = (j + i) /(j + k[arr[1]]) + 123123;
            i = i + subFunc(true);
        }
                void main(){
                do a = 1;
                while arr[arr[2]] == arr[arr[3]];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_whole_82(self):
        input = """void foo(){
            int i, k[1]; float j[10];
            i = k[j[10]];
        }
        int subFunc(boolean bl) {
            xyz = false;
            if(bl = false)
              xyz = true;
            else
              xyz = false;
            return 0;
        }
                void main(){
                int i,j,k[5];
                float arr[10];
                i = (j + i) /(j + k[arr[1]]) + 123123 + subFunc(true);
                do a = 1;
                while arr[arr[2]] == arr[arr[3]];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_whole_83(self):
        input = """void foo(){
            int i, k[1]; float j[10];
            i = k[j[10]];
            int x1;
            float x2;
            for(a = 10; a < 20; a = a + 1 )
                 i = i + 1;
        }
                void main(){
                int abc;
                continue;
                do a = 1;
                while arr[arr[2]] == arr[arr[3]];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_whole_84(self):
        input = """void foo(){
            int i, k[1]; float j[10];
            i = k[j[10]];
        }
                int[] func(boolean abc, float xyz) {
            int x1;
            float x2;
            for(a = 10; a < 20; a = a + 1 )
                 i = i + 1;
            if (a != 1)
              continue;
            else
              break;
          }
                void main(){
                do a = 1;
                while arr[arr[2]] == arr[arr[3]];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_whole_85(self):
        input="""
            float foo(float x, float y){
                x;
                foo(x+y);
                y;
            }
            boolean check(){
                if(a>x)
                return a;
                else
                if (a != 1)
                    for(a = 10; a < 20; a = a + 1 )
                        i = i + 1;
                else
                    foo(x+y);
                y;
            }
            void main() {
            int abc;
            int x,y;
            for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            return 0;
            }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_whole_86(self):
        input="""float foo(float x, float y){
                x;
                foo(x+y);
                y;
            }
            boolean check(){
                if(a>x)
                return a;
                else
                if (a != 1)
                    for(a = 10; a < 20; a = a + 1 )
                        i = i + 1;
                else
                    foo(x+y);
            }
            void main() {
            int abc;
            int x,y;
            for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            return 0;
            }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_whole_87(self):
        input="""float foo(float x, float y){
            x;
            foo(x+y);
            y;
        }
        boolean check(){
            if(a>x)
            return a;
            else
            if (a != 1)
                for(a = 10; a < 20; a = a + 1 )
                    i = i + 1;
            else
                x;
            y;
        }
        void main() {
        int abc;
        int x,y;
        for( abc = 1; xyz == true; abc = abc + 1)
            if(abc == 1)
                abc = 0;
            else
                do abc = abc + 1;
                while xyz != false;
        return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_whole_88(self):
        input="""float foo(float x, float y){
            x;
            foo(x+y);
            y;
        }
        boolean check(){
            if(a>x)
            return a;
            else
            if (a != 1)
                for(a = 10; a < 20; a = a + 1 )
                    i = i + 1;
            else
                x;
            y;
        }
        void main() {
        int abc;
        int x,y;
        for( abc = 1; xyz == true; abc = abc + 1)
            if(abc == 1)
                abc = 0;
            else
                do abc = abc + 1;
                while xyz != false;
        return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_whole_89(self):
        input="""boolean xyz;
        int abc;
        int subFunc(boolean bl) {
            xyz = false;
            do abc = abc + 1;
            while xyz != false;
            return 0;
        }
        float foo(float x, float y){
            x;
            foo(x+y);
            y;
        }
        boolean check(){
            if(a>x)
            return a;
            else
            if (a != 1)
                for(a = 10; a < 20; a = a + 1 )
                    i = i + 1;
            else
                foo(x+y);
            y;
        }
        void main() {
        int abc;
        int x,y;
        for( abc = 1; xyz == true; abc = abc + 1)
            if(abc == 1)
                abc = 0;
            else
                do abc = abc + 1;
                while xyz != false;
        return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_whole_90(self):
        input="""boolean xyz;
        int subFunc(boolean bl) {
            xyz = false;
            do abc = abc + 1;
            while xyz != false;
            return 0;
        }
        float foo(float x, float y){
            x;
            foo(x+y);
            y;
        }
        boolean check(){
            if(a>x)
            return a;
            else
            if (a != 1)
                for(a = 10; a < 20; a = a + 1 )
                    i = i + 1;
            else
                foo(x+y);
            y;
        }
        void main() {
        int abc;
        int x,y;
        for( abc = 1; xyz == true; abc = abc + 1)
            if(abc == 1)
                abc = 0;
            else
                do abc = abc + 1;
                while xyz != false;
        return 0;
        }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_whole_91(self):
        input="""boolean xyz;
            int abc;
            int subFunc(boolean bl) {
                xyz = false;
                do abc = abc + 1;
                while xyz != false;
                return 0;
            }
            float foo(float x, float y){
                x;
                foo(x+y);
                y;
            }
            boolean check(){
                if(a>x)
                return a;
                else
                if (a != 1)
                    for(a = 10; a < 20; a = a + 1 )
                        i = i + 1;
                else
                    foo(x+y);
                y;
            }
            void main() {
            int abc;
            int x,y;
            for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            return 0;
            }
            void main() {
            int abc;
            continue;

            }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_whole_92(self):
        input="""int abc, xyz;
            int subFunc(boolean bl) {
                xyz = false;
                do abc = abc + 1;
                while xyz != false;
                return 0;
            }
            float foo(float x, float y){
                x;
                foo(x+y);
                y;
            }
            boolean check(){
                if(a>x)
                return a;
                else
                if (a != 1)
                    for(a = 10; a < 20; a = a + 1 )
                        i = i + 1;
                else
                    foo(x+y);
                y;
            }
            void main() {
            int abc;
            int x,y;
            for( abc = 1; xyz == true; abc = abc + 1)
                if(abc == 1)
                    abc = 0;
                else
                    do abc = abc + 1;
                    while xyz != false;
            return 0;
            }"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_whole_93(self):
        input = """int func(boolean abc, float xyz) {
                      int x1;
                      float x2;
                      if (a != 1)
                        for(a = 10; a < 20; a = a + 1 )
                           i = i + 1;
                      else
                        break;
                      }
                      boolean check(){
                        if(a>x)
                          return a;
                        else
                          return x;
                }
                void main(){
                do a = 1;
                while arr[arr[2]] == arr[arr[3]];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_whole_94(self):
        input = """float foo(){
                    if (a<b)
                      a=a+1;
                    else
                      a-1;
                    }
                    boolean check(){
                    if(a>x)
                      return a;
                    else
                      return x;
                  }
                void main(){
                do a = 1;
                while arr[arr[2+x]] == arr[arr[3+y]];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_whole_95(self):
        input = """float foo(float x, float y){
                    x;
                    foo(x+y);
                    y;
                }
                  boolean check(){
                    if(a>x)
                      return a;
                    else
                      if (a != 1)
                        for(a = 10; a < 20; a = a + 1 )
                            i = i + 1;
                      else
                        break;
                }
                void main(){
                do a = 1;
                while arr[arr[2]] == arr[arr[3]];
                for( abc = 1; xyz == true; abc = abc + 1)
                  if(abc == 1)
                    abc = 0;
                  else
                    do abc = abc + 1;
                    while xyz != false;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_whole_96(self):
        input = """void foo(){
            int i, k[1]; float j[10];
            i = k[j[10]];
        }
         boolean check(){
            if(a>x)
              return a;
            else
              if (a != 1)
                for(a = 10; a < 20; a = a + 1 )
                    i = i + 1;
              else
                x;
            foo(x+y);
          }
        void foo ( int i ) {
            int i,j,k[5];
            i = (j + i) /(j + k[arr[1]]) + 123123;
            i = i + subFunc(true);
        }
                void main(){
                do a = 1;
                while arr[arr[2]] == arr[arr[3]];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_whole_97(self):
        input = """float foo(float x, float y){
                    x;
                    foo(x+y);
                    y;
                }
                  boolean check(){
                    if(a>x)
                      return a;
                    else
                      if (a != 1)
                        for(a = 10; a < 20; a = a + 1 )
                            i = i + 1;
                      else
                        foo(x+y);
                }
                  void main() {
                  int abc;
                  int x,y;
                  for( abc = 1; xyz == true; abc = abc + 1)
                      if(abc == 1)
                        abc = 0;
                      else
                        do abc = abc + 1;
                        while xyz != false;
                  return 0;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
