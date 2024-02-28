import unittest
from TestUtils import TestChecker

class CheckerSuite(unittest.TestCase):

    def test_static_check_0(self):
        input = """
            a: auto;
        """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_static_check_1(self):
        input = """
            a: integer = 1;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_static_check_2(self):
        input = """
            a: integer = 1.2;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_static_check_3(self):
        input = """
            a: auto = 1;
            b: integer = 2.0%a;
        """
        expect = "Type mismatch in expression: BinExpr(%, FloatLit(2.0), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_static_check_4(self):
        input = """
            a: auto = 2;
            a: integer = b;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test_static_check_5(self):
        input = """
            a: auto = func(2);
        """
        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_static_check_6(self):
        input = """
            a: array [2,3] of integer = {1,2.0,3};
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.0), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_static_check_7(self):
        input = """
            a: array [2] of float = {1, 1 ,3};
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], FloatType), ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test_static_check_8(self):
        input = """
            a: array [2] of integer = {2.0,3.2};
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([FloatLit(2.0), FloatLit(3.2)]))"
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test_static_check_9(self):
        input = """
            a: array [2,3] of integer = {{1,2,3},{4,5,6}};
            b: auto;
        """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_static_check_10(self):
        input = """
            a: array [2,3] of float = {{1,2,3}, {2.0,3.0,2.1}};
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([FloatLit(2.0), FloatLit(3.0), FloatLit(2.1)])])"
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test_static_check_11(self):
        input = """
            a: array [2,3] of float = {{1,2,3},{1,2,3.0}};
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test_static_check_12(self):
        input = """
            a: string = "1,2,3"::"2,4,5" + 3;
        """
        expect = "Type mismatch in expression: BinExpr(+, StringLit(2,4,5), IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test_static_check_13(self):
        input = """
            a: float = 1+2+3;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test_static_check_14(self):
        input = """
            a: float = 1+2+3.0 - 5 + 6;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_static_check_15(self):
        input = """
            a: auto = 1+2 - 3.0;
            b: integer = a + 4.0;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, Id(a), FloatLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test_static_check_16(self):
        input = """
            a: auto = 1::"1" -3.0%2;
        """
        expect = "Type mismatch in expression: BinExpr(%, FloatLit(3.0), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test_static_check_17(self):
        input = """
            a: auto = b;
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_static_check_18(self):
        input = """
            func: function integer() {
                a: integer = 1;
            }

        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_static_check_19(self):
        input = """
            func: function void (a: integer, a: auto) {
                
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_static_check_20(self):
        input = """
            func: function void(a: auto) {
                b: float = a + 2;
                c: float = a::"sb";
            }
        """
        expect = "Type mismatch in expression: BinExpr(::, Id(a), StringLit(sb))"
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_static_check_21(self):
        input = """
            b: integer = 2;
            func: function void(a: auto) {
                a = b;
                a= a::2;
            }
        """
        expect = "Type mismatch in expression: BinExpr(::, Id(a), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_static_check_22(self):
        input = """
            func: function void(a: auto) {
                a = b;
                a= a::2;
            }
            b: integer = 2;
        """
        expect = "Type mismatch in expression: BinExpr(::, Id(a), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_static_check_23(self):
        input = """
            func: function void (inherit a: integer, a: float) {
            
            }
            func2: function void (a: float) inherit func {
            
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_static_check_24(self):
        input = """
            func: function void (inherit a: integer, b: float) {
            
            }
            func2: function void (a: float) inherit func {
                super(1,2);
            }
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test_static_check_25(self):
        input = """
            func2: function void (a: float) inherit func {
                super(1,2);
            }
            func: function void (inherit a: integer, a: float) {
            
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_static_check_26(self):
        input = """
            func2: function void (a: float) inherit func {
                super(1,2);
            }
            func: function void (inherit a: integer, b: float) {
            
            }
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test_static_check_27(self):
        input = """
            func2: function void () {
                func(1.2);
            }
            func: function void (a: auto) {
                a = 5;
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test_static_check_28(self):
        input = """
            func: function void() inherit a {
                super();
            }
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 428))
    
    def test_static_check_29(self):
        input = """
        func: function void() inherit a {
            
        }
        """
        expect = "Invalid statement in function: func"
        self.assertTrue(TestChecker.test(input, expect, 429))
    
    def test_static_check_30(self):
        input = """
        inhr: function void(inherit a: auto) {}
        func: function void() inherit inhr {
            super(2);
            a = 2.3;
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), FloatLit(2.3))"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_static_check_31(self):
        input = """
        inhr: function void(inherit a: auto) {}
        func: function void() inherit inhr {
            preventDefault();
            a = 2.3;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_static_check_32(self):
        input = """
        inhr: function void(inherit a: auto) {}
        func: function void() inherit inhr {
            a = 2.3;
            preventDefault();
        }
        """
        expect = "Invalid statement in function: func"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_static_check_33(self):
        input = """
        a: array[2,3] of integer = {{1,2,3}, {4,5,6}};
        b: array[3] of integer = a[1];
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_static_check_34(self):
        input = """
        a: array[2,3] of integer = {{1,2,3}, {4,5,6}};
        b: array[3] of float = a[1];
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([3], FloatType), ArrayCell(a, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_static_check_35(self):
        input = """
        main: function integer() {}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_static_check_36(self):
        input = """
        main: function void() {
            for (a = {1,"1,2",3}, a < 10, a + 1) {
            
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_static_check_37(self):
        input = """
        main: function void() {
            a: integer;
            for (a = {1,"1,2",3}, a < 10, a + 1) {
            
            }
        }
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), StringLit(1,2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_static_check_38(self):
        input = """
        main: function void() {
            a: integer;
            for (a = {1,2,3}, a < 10, a + 1) {
            
            }
        }   
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 438))
    
    def test_static_check_39(self):
        input = """
        main: function void() {
            a: auto = 2;
            for (a = 1.2, a < 10, a + 1) {
            
            }
        }  
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_static_check_40(self):
        input = """
        main: function void() {
            a: integer;
            for (a = 1, a < 10, a + 1) {
                
            }
            break;
        }  
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 440))
    
    def test_static_check_41(self):
        input = """
        main: function void() {
            a: integer;
            if (a == 2) {
                if (a == 3) {
                    break;
                    for (a = 1, a < 1, a + 2) {}
                }
            }
        }  
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_static_check_42(self):
        input = """
        main1: function void() {
            a: integer;
            if (a == 2) {
                if (a == 3) {
                    for (a = 1, a < 1, a + 2) {
                        if (a == 5) break;
                    }
                }
            }
        }  
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_static_check_43(self):
        input = """
        main: function void() {
            i:integer;
            a:float = 2;
            for (i = 0, i+1, a+2) {}
        }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(a), IntegerLit(2)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test_static_check_44(self):
        input = """
        main: function void() {
            i:integer;
            a:float = 2;
            for (i = 0, true, {1,"2",3}) {}
        }
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), StringLit(2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_static_check_45(self):
        input = """
        a: function auto() {}
        b: function auto() {}
        main: function void () {
            c: array[2] of float = {a(), b()};
            printInteger(a());

        }
        """
        expect = "Type mismatch in statement: CallStmt(printInteger, FuncCall(a, []))"
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_static_check_46(self):
        input = """
            main: function void(){
        
            }
            a: integer;
            main: integer;
        """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test_static_check_47(self):
        input = """
        main: function void(c: integer, a: float){
            a: integer;
    
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_static_check_48(self):
        input = """
        func: function auto () {
            a: integer = 3;
            return a;
        }
        main: function void () {
            a: string = func()::"abc";
        }
        """
        expect = "Type mismatch in expression: BinExpr(::, FuncCall(func, []), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test_static_check_49(self):
        input = """
        a: auto = 1::"string";
        """
        expect = "Type mismatch in expression: BinExpr(::, IntegerLit(1), StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test_static_check_50(self):
        input = """
        a: auto = "string"::"string";
        c: integer = a;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_static_check_51(self):
        input = """
        func: function void () {
            return 3;
        }

        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_static_check_52(self):
        input = """
        func: function void () {
            a: integer = 3;
            return;
            return a;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_static_check_53(self):
        input = """
        func: function void () {
            a: integer = 3;
            if (a > 3) return;
            else return a;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_static_check_54(self):
        input = """
        main: function void () {
            a: auto = readInteger();
            printInteger(a);
            return 3;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_static_check_55(self):
        input = """
        func: function void (inherit a: integer) {}
        func123: function void () inherit func {
            preventDefault();
            a = 5;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_static_check_56(self):
        input = """
        func: function void (inherit a: integer) {}
        func123: function void () inherit func {
            super(2);
            a = 5;
        }   
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_static_check_57(self):
        input = """
        var: auto = a[12,3];
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_static_check_58(self):
        input = """
        a: integer = 3;
        var: auto = a[1,2,3,4];
        """
        expect = "Type mismatch in expression: ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])"
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test_static_check_59(self):
        input = """
        b: auto = {1,2,3};
        var: auto = b[1,"2"];
        """
        expect = "Type mismatch in expression: ArrayCell(b, [IntegerLit(1), StringLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test_static_check_60(self):
        input = """
        a: integer;
        a: float;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test_static_check_61(self):
        input = """
        main: function void() {
            a: integer = 5.3;
            {
                a: float;
            }
            a: string = 5;
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(5.3))"
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test_static_check_62(self):
        input = """
        func: function auto (a: auto, b: auto) {
            a = 3;
            b = 4.5;
            return "abc";
        }

        main: function void () {
            func(4.5, 3);
        }
        """
        expect = "Type mismatch in statement: CallStmt(func, FloatLit(4.5), IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_static_check_63(self):
        input = """
        func: function auto (a: auto, b: auto) {
            a = 3;
            b = 4.5;
            return "abc";
        }

        main: function void () {
            a:float = func(1, 3.2);
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, FloatType, FuncCall(func, [IntegerLit(1), FloatLit(3.2)]))"
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test_static_check_64(self):
        input = """
        func: function auto () {
        
        }
        var: array[3,2] of integer = {{1,2},{2,3},{func(),5}};
        var2: string = func();
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(var2, StringType, FuncCall(func, []))"
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_static_check_65(self):
        input = """
        main: function void() {
            var: integer = - "1cbsi";
        }
        """
        expect = "Type mismatch in expression: UnExpr(-, StringLit(1cbsi))"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_static_check_66(self):
        input = """
        main: function void() {
            a: string = "1e927e";
            var: integer = - a;
        }
        """
        expect = "Type mismatch in expression: UnExpr(-, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_static_check_67(self):
        input = """
        a: auto = {1,2,3,{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            for (a = {1,2,3}, a < {1,2,3}, a + {1,2,3}) {
                
            }
            if ({1,2,3}) {
            
            }
            else {
            
            }
            do {
            
            }
            while({1,2,3});
            while({1,2,3}) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)])])"
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test_static_check_68(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            for (a = {1,2,3}, a < {1,2,3}, a + {1,2,3}) {
                
            }
            if ({1,2,3}) {
            
            }
            else {
            
            }
            do {
            
            }
            while({1,2,3});
            while({1,2,3}) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_static_check_69(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, a < {1,2,3}, a + {1,2,3}) {
                
            }
            if ({1,2,3}) {
            
            }
            else {
            
            }
            do {
            
            }
            while({1,2,3});
            while({1,2,3}) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in expression: BinExpr(<, Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test_static_check_70(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, {1,2,3}, a + {1,2,3}) {
                
            }
            if ({1,2,3}) {
            
            }
            else {
            
            }
            do {
            
            }
            while({1,2,3});
            while({1,2,3}) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test_static_check_71(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, {1,2,3}) {
                
            }
            if ({1,2,3}) {
            
            }
            else {
            
            }
            do {
            
            }
            while({1,2,3});
            while({1,2,3}) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BooleanLit(True), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_static_check_72(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (1.2) {
            
            }
            else {
            
            }
            do {
            
            }
            while({1,2,3});
            while({1,2,3}) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in statement: IfStmt(FloatLit(1.2), BlockStmt([]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test_static_check_73(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (1.2) {
            
            }
            else {
            
            }
            do {
            
            }
            while({1,2,3});
            while({1,2,3}) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in statement: IfStmt(FloatLit(1.2), BlockStmt([]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test_static_check_74(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (true) {
            
            }
            else {
            
            }
            do {
            
            }
            while({1,2,3});
            while({1,2,3}) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in statement: DoWhileStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test_static_check_75(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (true) {
            
            }
            else {
            
            }
            do {
            
            }
            while(true);
            while({1,2,3}) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in statement: WhileStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test_static_check_76(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (true) {
            
            }
            else {
            
            }
            do {
            
            }
            while(true);
            while(true) {}
            break;
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test_static_check_77(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (true) {
            
            }
            else {
            
            }
            do {
            
            }
            while(true);
            while(true) {break;}
            
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test_static_check_78(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (true) {
            
            }
            else {
            
            }
            do {
                if (i == 3) continue;
            }
            while(true);
            while(true) {break;}
            
            
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test_static_check_79(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (true) {
            
            }
            else {
            
            }
            do {
                if (i == 3) continue;
            }
            while(true);
            while(true) {break;}
            
            
            return;
            return 1;
            func(1,2,3.5);
            bo: boolean = readBoolean();
        }
        """
        expect = "Type mismatch in statement: CallStmt(func, IntegerLit(1), IntegerLit(2), FloatLit(3.5))"
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test_static_check_80(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (true) {
            
            }
            else {
            
            }
            do {
                if (i == 3) continue;
            }
            while(true);
            while(true) {break;}
            
            
            return;
            return 1;
            func(1,2,3);
            bo: boolean = readBoolean(2);
        }
        """
        expect = "Type mismatch in expression: FuncCall(readBoolean, [IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test_static_check_81(self):
        input = """
            //var : string = foo(1.0, 2.3,23);
            foo : function auto (inherit out z : auto, t:auto) inherit func{
                z = 5;
                return z + t;
            }
            a : auto = foo(2.0, 2);
            b : auto = foo(3.0, 1);
            c : float = a + b;
            main : function void() {}
            func : function void() {}
        """
        expect = "Type mismatch in expression: FuncCall(foo, [FloatLit(2.0), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_static_check_82(self):
        input = """
        func: function void () {
            return 3;
        }

        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_static_check_83(self):
        input = """
            a: auto = 1::"1" -3.0%2;
        """
        expect = "Type mismatch in expression: BinExpr(%, FloatLit(3.0), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_static_check_84(self):
        input = """
            func: function void (inherit a: integer, b: float) {
            
            }
            func2: function void (a: float) inherit func {
                super(1,2);
            }
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_static_check_85(self):
        input = """
            a: float = 1+2+3;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_static_check_86(self):
        input = """
            func: function void() inherit a {
                super();
            }
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_static_check_87(self):
        input = """
        main: function void(c: integer, a: float){
            a: integer;
    
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_static_check_88(self):
        input = """
        main: function void () {
            a: auto = readInteger();
            printInteger(a);
            return 3;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_static_check_89(self):
        input = """
        main: function void() {
            var: integer = - "1cbsi";
        }
        """
        expect = "Type mismatch in expression: UnExpr(-, StringLit(1cbsi))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_static_check_90(self):
        input = """
        main: function void() {
            i:integer;
            a:float = 2;
            for (i = 0, i+1, a+2) {}
        }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(a), IntegerLit(2)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_static_check_91(self):
        input = """
        a: integer = 3;
        var: auto = a[1,2,3,4];
        """
        expect = "Type mismatch in expression: ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_static_check_92(self):
        input = """
        a: auto = {{1,2,3},{2,3,4}};
        func: function void (a: integer, b: integer, c:integer) {}
        main: function void () {
            i:integer;
            for (i = 1, true, 1) {
                
            }
            if (true) {
            
            }
            else {
            
            }
            do {
            
            }
            while(true);
            while(true) {break;}
            
            continue;
            return a;
            func(1,2,3);
            bo: boolean = readBoolean();
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_static_check_93(self):
        input = """
            a: auto = 2;
            a: integer = b;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_static_check_94(self):
        input = """
            a: float = 1+2+3.0 - 5 + 6;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_static_check_95(self):
        input = """
        main1: function void() {
            a: integer;
            if (a == 2) {
                if (a == 3) {
                    for (a = 1, a < 1, a + 2) {
                        if (a == 5) break;
                    }
                }
            }
        }  
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_static_check_96(self):
        input = """
        a: auto = "string"::"string";
        c: integer = a;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_static_check_97(self):
        input = """
            func: function void (a: integer, a: auto) {
                
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_static_check_98(self):
        input = """
            a: array [2,3] of integer = {1,2.0,3};
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.0), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_static_check_99(self):
        input = """
        inhr: function void(inherit a: auto) {}
        func: function void() inherit inhr {
            super(1,2,3);
            a = 2.3;
        }
        """
        expect = "Type mismatch in expression: IntegerLit(2)"
        self.assertTrue(TestChecker.test(input, expect, 499))
