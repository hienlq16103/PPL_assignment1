import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_no_declaration_0(self):
        input = ''''''
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_no_declaration_1(self):
        input = '''## Hello world'''
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() return 1
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_wrong_declaration(self):
        input = """var aPI <- 3.14"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 206))
    #================== DECLARATION TEST ===================
    #------------------ variable declaration test ----------
    def test_variable_declaration_0(self):
        input = '''number x
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_variable_declaration_1(self):
        input = """string str
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_variable_declaration_2(self):
        input = """bool isValid
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_variable_declaration_3(self):
        input = """dynamic div
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_variable_declaration_4(self):
        input = """int x
        """
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_variable_declaration_5(self):
        input = """number 1variable
        """
        expect = "Error on line 1 col 7: 1"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_variable_declaration_6(self):
        input = """number variable@
        """
        expect = "@"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_variable_declaration_7(self):
        input = """## This is my program
        number variable
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_variable_declaration_8(self):
        input = """number x <- 1 ## initialize variable's value"""
        expect = "Error on line 1 col 44: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_variable_declaration_9(self):
        input = '''number x <- 1 ## initialize variable's value
        '''
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_variable_declaration_10(self):
        input = '''
        number x <- 1
        '''
        expect = "Error on line 1 col 0: \n\n"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_variable_declaration_11(self):
        input = '''## my program
        number x <- 1
        bool isValid <- true ## flag
        string str <- "Hello world"
        '''
        expect = "Error on line 4 col 8: string"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_variable_declaration_12(self):
        input = '''## my program
        number x <- 1
        
        
        bool isValid <- true 
        
        string str <- "Hello world"
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_variable_declaration_13(self):
        input = '''## my program
        number x <- true
        
        
        bool isValid <- 1.1 
        
        string str <- "Hello world"
        dynamic k <- false
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_variable_declaration_14(self):
        input = '''## my program
        number x <- true
        
        
        bool isValid <- +.1e13 
        
        string str <- "Hello world"
        dynamic k <- false
        '''
        expect = "."
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_variable_declaration_15(self):
        input = '''## my program
        var x
        '''
        expect = "Error on line 2 col 13: \n\n"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_variable_declaration_16(self):
        input = '''## my program
        var x
        '''
        expect = "Error on line 2 col 13: \n\n"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_variable_declaration_17(self):
        input = '''## my program
        var x <- "Nothing is true, everything is permitted"
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_variable_declaration_18(self):
        input = '''## my program
        var x <- "Nothing is true, \\everything is permitted"
        '''
        expect = "Nothing is true, \\e"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_variable_declaration_19(self):
        input = '''## my program
        number x, y, z
        '''
        expect = "Error on line 2 col 16: ,"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_variable_declaration_20(self):
        input = '''## my program
        number x[5]
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_variable_declaration_21(self):
        input = '''## my program
        number x[5] <- [1,2,3,4,5]
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_variable_declaration_22(self):
        input = '''## my program
        number x[5] <- [true,"str"]
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_variable_declaration_23(self):
        input = '''## my program
        number x[5,6] <- [true,"str",]
        '''
        expect = "Error on line 2 col 37: ]"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_variable_declaration_24(self):
        input = '''## my program
        number x[5,6] <- []
        '''
        expect = "Error on line 2 col 26: ]"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_variable_declaration_25(self):
        input = '''## my program
        number x[5,6,] <- []
        '''
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_variable_declaration_26(self):
        input = '''## my program
        number x[5,6] <- [[1,2,3]]
        '''
        expect = "Error on line 2 col 33: ]"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_variable_declaration_27(self):
        input = '''## my program
        number x[5,6] <- [[1,2,3],[5,6]]
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_variable_declaration_28(self):
        input = '''## my program
        number x[5,6] <- [[],[]]
        '''
        expect = "Error on line 2 col 27: ]"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_variable_declaration_29(self):
        input = '''## my program
        number x[true] <- [[1,2],[3,true]]
        '''
        expect = "Error on line 2 col 17: true"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_variable_declaration_30(self):
        input = '''## my program
        var x[1] <- [[1,2],[3,true]]
        '''
        expect = "Error on line 2 col 13: ["
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_variable_declaration_31(self):
        input = '''## my program
        bool x[1][2] <- [[1,2],[3,true]]
        '''
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 238))
        
    #------------------ function declaration test ----------
    def test_function_delcaration_0(self):
        input = '''## my program
        func foo()
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_function_delcaration_1(self):
        input = '''## my program
        func foo() return
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_function_delcaration_2(self):
        input = '''## my program
        func foo() 
        return
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_function_delcaration_3(self):
        input = '''## my program
        func foo() 
        
        
        return
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_function_delcaration_4(self):
        input = '''## my program
        func foo() begin
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_function_delcaration_5(self):
        input = '''## my program
        func foo() begin
        
        
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_function_delcaration_6(self):
        input = '''## my program
        func foo() begin end
        '''
        expect = "Error on line 2 col 25: end"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_function_delcaration_7(self):
        input = '''## my program
        func foo(number a, bool b) begin 
            ## begin function
            return true
            
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_function_delcaration_8(self):
        input = '''## my program
        func foo(number a, bool b[]) begin 
            ## begin function
            return true
            
        end
        '''
        expect = "Error on line 2 col 34: ]"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_function_delcaration_9(self):
        input = '''## my program
        func foo(number a, bool b[5]) begin 
            ## begin function
            return true
            
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_function_delcaration_10(self):
        input = '''## my program
        func foo(number a, bool b[5],) begin 
            ## begin function
            return true
            
        end
        '''
        expect = "Error on line 2 col 37: )"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_function_delcaration_11(self):
        input = '''## my program
        func foo(number a <- 1.1, bool b[5]) 
        '''
        expect = "Error on line 2 col 26: <-"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_function_delcaration_12(self):
        input = '''## my program
        func foo(number a, bool b[5])
            begin
                begin
                
                end
            end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_function_delcaration_13(self):
        input = '''## my program
        func foo(number a, number b)
            number sum <- a + b
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_function_delcaration_14(self):
        input = '''## my program
        func foo(number a, number b)
            max()
        '''
        expect = "Error on line 3 col 12: max"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_function_delcaration_15(self):
        input = '''## my program
        func foo(number a, number b)'''
        expect = "Error on line 2 col 36: <EOF>"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_function_delcaration_16(self):
        input = '''## my program
        func foo(number a, number b)'''
        expect = "Error on line 2 col 36: <EOF>"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_function_delcaration_17(self):
        input = '''## my program
        func foo(var a, number b)
        '''
        expect = "Error on line 2 col 17: var"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_function_delcaration_18(self):
        input = '''## my program
        func foo(number a, number b) 
        begin
        end'''
        expect = "Error on line 4 col 11: <EOF>"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_function_delcaration_19(self):
        input = '''## my program
        func foo(number a, number b) 
        return 1'''
        expect = "Error on line 3 col 16: <EOF>"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_function_delcaration_20(self):
        input = '''## my program
        func foo(number a, number b) 
        return (a+b)
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_function_delcaration_21(self):
        input = '''## my program
        func foo(number a, number b) return (a+b)
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))   
        
    #================== STATEMENT TEST ===================
    def test_statement_0(self):
        input = '''## my program
        func main()
        begin
            pi <- 3.14
            a[3] <- 2*6+9
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260)) 
    def test_statement_1(self):
        input = '''## my program
        func main()
        begin
            pi <- 3.14
            a[3] <- 2*6+9 end
        '''
        expect = "Error on line 5 col 26: end"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_statement_2(self):
        input = '''## my program
        func main()
        begin
            ## assign pi value
            pi <- 3.14
            a[3] <- 2*6+9 
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262)) 
    def test_statement_3(self):
        input = '''## my program
        func main()
        begin
            ## assign pi value
            pi <- 3.14 ## in line comment
            a[3] <- 2*6+9 
        end
        '''
        expect = "Error on line 6 col 12: a"
        self.assertTrue(TestParser.test(input,expect,263)) 
    def test_statement_4(self):
        input = '''## my program
        func main()
        begin
            ## assign pi value
            
            pi <- 3.14
            
            F()[3] <- 2*6+9 
        end
        '''
        expect = "Error on line 8 col 15: ["
        self.assertTrue(TestParser.test(input,expect,264)) 
    def test_statement_5(self):
        input = '''## my program
        func max(number a, number b)
        begin
            number max <- a
            if (a < b) max <- b
            return max
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265)) 
    def test_statement_6(self):
        input = '''## my program
        func max(number a, number b, number c)
        begin
            if (a >= b) begin
                if (a >= c) return a
                else return c
            end
            else if (b >= c)
                return b
            else 
                return c
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_statement_7(self):
        input = '''## my program
        func max(number a, number b, number c)
        begin
            if (a >= b) begin
                if (a >= c) return a
                else return c
            end
            elif (b >= c)
                return b
            else 
                return c
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267)) 
    def test_statement_8(self):
        input = '''## my program
        func main() begin
            if (a = true)
                continue
            if (b = false)
                break
            else return
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268)) 
    def test_statement_9(self):
        input = '''## my program
        func main() begin
            if (a = true)
                continue
            if (b = false)
                break
            elif (true + true) a <- 3
            else return
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_statement_10(self):
        input = '''## my program
        func main() begin
            if (a = true) 
                if (b = true)
                    return true
                else return false
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_statement_11(self):
        input = '''## my program
        func main() begin
            if (true)
            return 
            elif (true)
            if (true)
            return
            else
            return
            else
            return false
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_statement_12(self):
        input = '''## my program
        func main() begin
            number sum <- 0
            number index <-0 
            for index until index >= 10 by 1
                sum <- sum + index
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_statement_13(self):
        input = '''## my program
        func main() begin
            number sum <- 0
            number index <-0 
            for index until index >= 10 by 1 sum <- sum + index
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_statement_14(self):
        input = '''## my program
        func main() begin
            number sum <- 0
            number index <-0 
            for index until index >= 10 by 1 sum <- sum + index end
        '''
        expect = "Error on line 5 col 64: end"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_statement_15(self):
        input = '''## my program
        func main() begin
            if (a<b) return'''
        expect = "Error on line 3 col 27: <EOF>"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_statement_16(self):
        input = '''## my program
        func main() begin
            if (a<b)
            else return true'''
        expect = "Error on line 4 col 12: else"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_statement_17(self):
        input = '''## my program
        func main() begin
            if (a<b) return false
            else return true'''
        expect = "Error on line 4 col 28: <EOF>"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_statement_18(self):
        input = '''## my program
        func main() begin
            if (a<b) return false
            else'''
        expect = "Error on line 4 col 16: <EOF>"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_statement_19(self):
        input = '''## my program
        func main() begin
            if (a<b) return false
            elif (a=b)
            else return false
            '''
        expect = "Error on line 5 col 12: else"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_statement_20(self):
        input = '''## my program
        func main() begin
            if (a<b) if (a>b)
            '''
        expect = "Error on line 4 col 12: <EOF>"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_statement_21(self):
        input = '''## my program
        func main() begin
            number array[5,5]
            number sum <- 0
            number i <- 0
            number j <- j
            for i until i >= 5 by 1
                for j until j >=5 by 1
                    sum <- sum + array[i,j]
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_statement_22(self):
        input = '''## my program
        func main() begin
            for i until i >= n by 1
        end
        '''
        expect = "Error on line 4 col 8: end"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_statement_23(self):
        input = '''## my program
        func main() begin
            break
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_statement_24(self):
        input = '''## my program
        func main() begin
            break end
        '''
        expect = "Error on line 3 col 18: end"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_statement_25(self):
        input = '''## my program
        func main() begin
            continue
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_statement_26(self):
        input = '''## my program
        func main() begin
            continue end
        '''
        expect = "Error on line 3 col 21: end"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_statement_27(self):
        input = '''## my program
        func main() begin
            return
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_statement_28(self):
        input = '''## my program
        func main() begin
            return 1
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_statement_29(self):
        input = '''## my program
        func main() begin
            return 1 end
        '''
        expect = "Error on line 3 col 21: end"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_statement_30(self):
        input = '''## my program
        func main() begin
            return end
        '''
        expect = "Error on line 3 col 19: end"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_statement_31(self):
        input = '''## my program
        func main() begin
            foo()
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_statement_32(self):
        input = '''## my program
        func main() begin
            foo(foo1(a,b,c),1,15,(1+1))
        
        '''
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_statement_33(self):
        input = '''## my program
        func main() begin
            foo(foo1(a,b,c),1,true,(1+1),"123",array[5])
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
    #================== EXPRESSION TEST ===================
    def test_expression_0(self):
        input = '''## my program
        func main() begin
            a[3 + foo(2)] <- a[b[2, 3]] + 4
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_expression_1(self):
        input = '''## my program
        func main() begin
            a[3 + foo(2)] <- a[b[2, 3]] + 4
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_expression_1(self):
        input = '''## my program
        func main() begin
            return (a+b)*c + (-e-f) /(5 % foo())
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_expression_2(self):
        input = '''## my program
        func main() begin
            return not not not -----c
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_expression_3(self):
        input = '''## my program
        func main() begin
            return -a -b-c + 1*2*3*4 + (a and b[1,2] and foo()[1])
        end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_expression_4(self):
        input = '''## my program
        func main() begin
            return "hello"..."world" ..."me"
        end
        '''
        expect = "Error on line 3 col 37: ..."
        self.assertTrue(TestParser.test(input,expect,299))
    def test_expression_4(self):
        input = '''## my program
        func main() begin
            return array[1][1]
        end
        '''
        expect = "Error on line 3 col 27: ["
        self.assertTrue(TestParser.test(input,expect,299))
    
    #================== PROGRAM TEST ====================
    def test_program_0(self):
        input = '''## my program
        func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
            end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,301))
    def test_program_1(self):
        input = '''## my program
        func isPrime(number x)
            begin
                if (x <= 1) return false
                var i <- 2
                for i until i > x / 2 by 1
                    begin
                        if (x % i = 0) return false
                    end
                return true
            end
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,302))
    def test_program_2(self):
        input = '''## my program
        for i until i >= len by 1
            if (i % 2 = 0) sum <- sum + i
        '''
        expect = "Error on line 2 col 8: for"
        self.assertTrue(TestParser.test(input,expect,303))