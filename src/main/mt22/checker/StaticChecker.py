from Visitor import Visitor
from StaticError import *
from AST import *
import copy

class Symbol: pass
class VarSymbol(Symbol):
    def __init__(self, name, typ, check=False):
        self.name = name
        self.typ = typ
        self.check=check

    def __str__(self):
        return "VarSymbol({}, {}, {})".format(self.name, str(self.typ), str(self.check))

class FuncSymbol(Symbol):
    def __init__(self, name, typ, params = [], inherit = None, check=False):
        self.name = name
        self.typ = typ
        self.params = params
        self.inherit = inherit
        self.check=check

    def __str__(self):
        return "FuncDecl({}, {}, [{}], {}, {})".format(self.name, str(self.typ), ", ".join([str(param) for param in self.params]), self.inherit if self.inherit else "None", str(self.check))

class GetEnv(Visitor):
    def __init__(self, ctx):
        self.ctx=ctx

    def visitProgram(self, ctx, o):
        o = []
        for decl in ctx.decls:
            self.visit(decl, o)
        return o
    
    def visitVarDecl(self, ctx, o):
        o += [VarSymbol(ctx.name, ctx.typ)]

    def visitFuncDecl(self, ctx, o): 
        o += [FuncSymbol(ctx.name, ctx.return_type, ctx.params, ctx.inherit)]
    def visitParamDecl(self, ctx, o): pass
    
    def visitAssignStmt(self, ctx, o): pass
    def visitBlockStmt(self, ctx, o):pass
    def visitIfStmt(self, ctx, o): pass
    def visitForStmt(self, ctx, o): pass
    def visitWhileStmt(self, ctx, o): pass
    def visitDoWhileStmt(self, ctx, o): pass
    def visitBreakStmt(self, ctx, o): pass
    def visitContinueStmt(self, ctx, o): pass
    def visitReturnStmt(self, ctx, o): pass
    def visitCallStmt(self, ctx, o): pass

    def visitBinExpr(self, ctx, o): pass
    def visitUnExpr(self, ctx, o): pass
    def visitId(self, ctx, o): pass
    def visitArrayCell(self, ctx, o): pass
    def visitIntegerLit(self, ctx, o): pass
    def visitFloatLit(self, ctx, o): pass
    def visitStringLit(self, ctx, o): pass
    def visitBooleanLit(self, ctx, o): pass
    def visitArrayLit(self, ctx, o): pass
    def visitFuncCall(self, ctx, o): pass
    
    def visitIntegerType(self, ctx, o): pass
    def visitFloatType(self, ctx, o): pass
    def visitBooleanType(self, ctx, o): pass
    def visitStringType(self, ctx, o): pass
    def visitArrayType(self, ctx, o): pass
    def visitAutoType(self, ctx, o): pass
    def visitVoidType(self, ctx, o): pass  

class Utils:
    def checkRedeclared(king, list, name):
        # checker = False
        for ele in list[0]:
            if ele.check and ele.name == name:
                # if checker:
                raise Redeclared(king, name)
                # else:
                #     checker = True
        # obj = Utils.getSymbol(list, name)
        # if obj is not None:
        #     obj.check=True
    
    def checkInvalidParam(list, name):
        for ele in list:
            if ele.name == name:
                raise Invalid(Parameter(), name)
    
    def checkUndeclared(king, list, name):
        if type(king) is Identifier:
            for ele in list:
                for item in ele:
                    if type(item) is VarSymbol and item.name == name:
                        return item
        elif type(king) is Function:
            for ele in list:
                for item in ele:
                    if type(item) is FuncSymbol and item.name == name:
                        return item
        else: return None
        raise Undeclared(king, name)
    
    def findInherit(list, name):
        res = []
        inherit = Utils.checkUndeclared(Function(), list, name).inherit
        if inherit is not None:
            func = Utils.checkUndeclared(Function(), list, inherit)

            for param in func.params:
                for ele in res:
                    if ele.name == param.name:
                        raise Redeclared(Parameter(), param.name)
                if param.inherit:
                    Utils.checkInvalidParam(res, param.name)
                    res.append(VarSymbol(param.name, param.typ, True))
        return res

    def getSymbol(list, name):
        for ele in list:
            for item in ele:
                if item.name == name:
                    return item
        return None
    
    def compareArrayType(a,b):
        if type(a) is type(b) and type(a) is ArrayType:
            if type(a.typ) is type(b.typ) and a.dimensions == b.dimensions:
                return True
        return False
    
    def infer(list, name, typ):
        for ele in list:
            for item in ele:
                if item.name == name:
                    item.typ = typ
                    return typ
                
    def compareType(a,b):
        if type(a) is type(b):
            if type(a) is ArrayType:
                return Utils.compareArrayType(a,b)
            return True
        return False
    
    def inferParam(list, name, param, typ):
        func = Utils.getSymbol(list, name)
        if func is not None and type(func) is FuncSymbol:
            for fparam in func.params:
                if fparam.name == param and type(fparam.typ) is AutoType:
                    fparam.typ = typ
                    return typ
        

class StaticChecker(Visitor):

    global_env = [FuncSymbol("readInteger", IntegerType()),
                  FuncSymbol("printInteger", VoidType(), [ParamDecl("anArg", IntegerType())]),
                  FuncSymbol("readFloat", FloatType(), []),
                  FuncSymbol("writeFloat", VoidType(), [ParamDecl("anArg", FloatType())]),
                  FuncSymbol("readBoolean", BooleanType()),
                  FuncSymbol("printBoolean", VoidType(), [ParamDecl("anArg", BooleanType())]),
                  FuncSymbol("readString", StringType()),
                  FuncSymbol("printString", VoidType(), [ParamDecl("anArg", StringType())])
                  ]

    def __init__(self, ctx):
        self.ctx = ctx

    def check(self):
        return self.visit(self.ctx, [])
    
    def visitProgram(self, ctx, o):

        env = [GetEnv(ctx).visit(ctx, o) + StaticChecker.global_env]

        for decl in ctx.decls:
            if type(decl) is VarDecl:
                self.visit(decl, (True,env))
            else:
                self.visit(decl, env)

        mainFunc = Utils.getSymbol(env, 'main')
        if mainFunc is None or type(mainFunc) is not FuncSymbol or len(mainFunc.params) != 0 or type(mainFunc.typ) is not VoidType:
            raise NoEntryPoint()
        return []
    
    def visitVarDecl(self, ctx, o):
        isGlobal, env = o
        if not isGlobal:
            env[0] += [VarSymbol(ctx.name, ctx.typ, False)]
        Utils.checkRedeclared(Variable(), env, ctx.name)
        Utils.getSymbol(env, ctx.name).check=True

        typ1 = ctx.typ
        if (type(typ1) is AutoType and ctx.init is None):
            raise Invalid(Variable(), ctx.name)

        if ctx.init is None: return

        if type(ctx.init) is ArrayLit:
            expect = copy.deepcopy(ctx.typ)
            typ2 = self.visit(ctx.init, (expect,env))
        else:
            typ2 = self.visit(ctx.init, env)

        if type(typ1) is AutoType:
            typ1 = Utils.infer(env, ctx.name, typ2)
        if type(typ2) is AutoType:
            typ2 = Utils.infer(env, ctx.init.name, typ1)

        if type(typ1) is FloatType and type(typ2) is IntegerType:
            return
        
        
        if not Utils.compareType(typ1,typ2):
            raise TypeMismatchInVarDecl(ctx)
        
        

    def visitFuncDecl(self, ctx:FuncDecl, o): 
        if ctx.name in ['super','preventDefault']:
            raise Redeclared(Function(), ctx.name)

        Utils.checkRedeclared(Function(), o, ctx.name) 

        func = Utils.checkUndeclared(Function(), o, ctx.name)
        func.check =True

        env = [[]] + o
        for param in func.params:
            self.visit(param, env)

        if ctx.inherit is not None:
            inheritFunc = Utils.getSymbol(env, ctx.inherit)
            if type(inheritFunc) is FuncSymbol:
                env[-1] += [FuncSymbol('super', VoidType(), inheritFunc.params), FuncSymbol('preventDefault', VoidType())]

                if len(inheritFunc.params) > 0:
                    if len(ctx.body.body) <= 0 or type(ctx.body.body[0]) is not CallStmt or ctx.body.body[0].name not in ['super', 'preventDefault']:
                        raise InvalidStatementInFunction(ctx.name)
                
                for idx, body in enumerate(ctx.body.body):
                    if type(body) is FuncCall and body.name in ['super', 'preventDefault'] and idx != 0:
                        raise InvalidStatementInFunction(ctx.name)
            else:
            
                if len(ctx.body.body) <= 0 or type(ctx.body.body[0]) is not CallStmt or ctx.body.body[0].name not in ['super', 'preventDefault']:
                        raise InvalidStatementInFunction(ctx.name)

        self.visit(ctx.body, (ctx.name,False,env))

        if len(ctx.params) <= 0: return
        func = Utils.checkUndeclared(Function(), env, ctx.name)
        if func is not None:

            for i in range(len(func.params)):
                if type(func.params[i].typ) is AutoType and func.params[i].name == env[0][i].name:
                    func.params[i].typ = env[0][i].typ

        
            
    def visitParamDecl(self, ctx, o): 
        Utils.checkRedeclared(Parameter(), o, ctx.name)
        o[0] += [VarSymbol(ctx.name, ctx.typ,True)]
    
    def visitAssignStmt(self, ctx, o):
        name,inLoop, env = o 
        typ1 = self.visit(ctx.lhs, env)


        if type(ctx.rhs) is ArrayLit:
            expect = typ1
            typ2 = self.visit(ctx.rhs, (expect,env))
        else:
            typ2 = self.visit(ctx.rhs, env)

        if type(typ1) is AutoType:
            typ1 = Utils.infer(env, ctx.lhs.name, typ2)
        if type(typ2) is AutoType:
            typ2 = Utils.infer(env, ctx.rhs.name, typ1)

        if type(typ1) is FloatType and type(typ2) is IntegerType:
            return
        
        if not Utils.compareType(typ1,typ2):
            raise TypeMismatchInStatement(ctx)
        
        
        return typ1

    def visitBlockStmt(self, ctx, o): 
        name,inLoop, env = o

        once = False
        for idx,body in enumerate(ctx.body):
            if type(body) is ReturnStmt:
                if not once:
                    once = True
                else:
                    del ctx.body[idx]
                    break

        for body in ctx.body:
            if type(body) is VarDecl:
                self.visit(body, (False,env))
            elif type(body) is BlockStmt:
                self.visit(body, (name, inLoop, [[]] + env))
            else:
                self.visit(body, o)

    def visitIfStmt(self, ctx, o): 
        name,inLoop, env = o
        if type(ctx.cond) is ArrayLit:
            self.visit(ctx.cond, (AutoType() ,env))
            raise TypeMismatchInStatement(ctx)
         
        typ = self.visit(ctx.cond, env)

        if type(typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        tenv = [[]] + env
        self.visit(ctx.tstmt, (name,inLoop, tenv))
        if ctx.fstmt is not None: 
            fenv = [[]] + env
            self.visit(ctx.fstmt, (name,inLoop, fenv))
            # self.visit(ctx.fstmt, o)
    def visitForStmt(self, ctx, o): 
        name,inLoop, env = o
        if type(self.visit(ctx.init, o)) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        
        if type(ctx.cond) is ArrayLit:
            self.visit(ctx.cond, (AutoType() ,env))
            raise TypeMismatchInStatement(ctx)
        if type(ctx.upd) is ArrayLit:
            self.visit(ctx.upd, (AutoType() ,env))
            raise TypeMismatchInStatement(ctx)
        
        if type(self.visit(ctx.cond,env)) is not BooleanType or type(self.visit(ctx.upd,env)) is not IntegerType:
            raise TypeMismatchInStatement(ctx)

        env1 = [[]] + env
        self.visit(ctx.stmt, (name,True,env1))
    def visitWhileStmt(self, ctx, o): 
        name,inLoop, env = o

        if type(ctx.cond) is ArrayLit:
            self.visit(ctx.cond, (AutoType() ,env))
            raise TypeMismatchInStatement(ctx)
        
        if type(self.visit(ctx.cond,env)) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        env1 = [[]] + env
        self.visit(ctx.stmt, (name,True,env1))
    def visitDoWhileStmt(self, ctx, o): 
        name,inLoop, env = o

        if type(ctx.cond) is ArrayLit:
            self.visit(ctx.cond, (AutoType() ,env))
            raise TypeMismatchInStatement(ctx)
        
        if type(self.visit(ctx.cond,env)) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        
        env1 = [[]] + env
        self.visit(ctx.stmt, (name,True,env1))
    def visitBreakStmt(self, ctx, o): 
        name,inLoop, env = o

        if not inLoop:
            raise MustInLoop(ctx)
    def visitContinueStmt(self, ctx, o):
        name,inLoop, env = o

        if not inLoop:
            raise MustInLoop(ctx)
    def visitReturnStmt(self, ctx, o): 
        name,inLoop, env = o

        funcTyp = Utils.getSymbol(env, name).typ
        if ctx.expr is not None: 
            if type(ctx.expr) is ArrayLit:
                expect = funcTyp.typ
                rtyp = self.visit(ctx.expr, (expect ,env))

            else:
                rtyp = self.visit(ctx.expr, env)
        else:
            rtyp = VoidType()

        if type(funcTyp) is AutoType:
            funcTyp = Utils.infer(env, name, rtyp)
        if type(rtyp) is AutoType:
            rtyp = Utils.infer(env, ctx.expr.name, funcTyp)

        if type(funcTyp) is FloatType and type(rtyp) is IntegerType:
            return
        if not Utils.compareType(funcTyp,rtyp):
            raise TypeMismatchInStatement(ctx)
       
    def visitCallStmt(self, ctx, o):
        name,inLoop, env = o

        if ctx.name in ['super', 'preventDefault']:
            funct = Utils.checkUndeclared(Function(), env, name)
 
            if funct.inherit is not None:
                Utils.checkUndeclared(Function(), env, funct.inherit)
        func = Utils.checkUndeclared(Function(), env, ctx.name)

        if type(func.typ) is AutoType:
            Utils.infer(env, ctx.name, VoidType())

        if len(ctx.args) == len(func.params):
            for i in range(len(ctx.args)):
                typParam = func.params[i].typ
                if type(ctx.args[i]) is ArrayLit:
                    expect = typParam
                    typArgs = self.visit(ctx.args[i], (expect, env))
                else:
                    typArgs = self.visit(ctx.args[i], env)
                
                if type(typArgs) is IntegerType and type(typParam) is FloatType:
                    continue
                if type(func.params[i].typ) is not AutoType and not Utils.compareType(typArgs, typParam):
                    if ctx.name == 'super':
                        raise TypeMismatchInExpression(ctx.args[i])
                    raise TypeMismatchInStatement(ctx)
                if type(func.params[i].typ) is AutoType:
                    Utils.inferParam(env, ctx.name, func.params[i].name, typArgs)
                    if (ctx.name == 'super'):
                        funct = Utils.checkUndeclared(Function(), env, name).inherit
                        Utils.inferParam(env, funct, func.params[i].name, typArgs)
                    Utils.infer(env, func.params[i].name, typArgs)

        else:
            if ctx.name == 'super':
                if len(ctx.args) < len(func.params):
                    raise TypeMismatchInExpression(None)
                else:
                    raise TypeMismatchInExpression(ctx.args[len(func.params)])

            if ctx.name in ['super', 'preventDefault']:
                raise InvalidStatementInFunction(name)
            raise TypeMismatchInStatement(ctx) 
        
        if ctx.name == 'super':
            funct = Utils.checkUndeclared(Function(), env, name)
            if funct.inherit is not None:
                inheritParams = Utils.findInherit(env,funct.name)

                for param in funct.params:
                    Utils.checkInvalidParam(inheritParams, param.name)
                
                env[0] += inheritParams
    def visitBinExpr(self, ctx:BinExpr, o): 
        if type(ctx.left) is ArrayLit:
            expect = ctx.left
            self.visit(ctx.left, (AutoType(),o))
            raise TypeMismatchInExpression(ctx)
        if type(ctx.right) is ArrayLit:
            expect = ctx.right
            self.visit(ctx.right, (AutoType(),o))
            raise TypeMismatchInExpression(ctx)

        typ1 = self.visit(ctx.left, o)
        typ2 = self.visit(ctx.right, o)
        if type(typ1) is AutoType:
            typ1 = Utils.infer(o, ctx.left.name, typ2)
        if type(typ2) is AutoType:
            typ2 = Utils.infer(o, ctx.right.name, typ1)

        if ctx.op in ['+', '-', '*', '/']:
            if type(typ1) is not IntegerType and type(typ1) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            if type(typ2) is not IntegerType and type(typ2) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            if type(typ1) is type(typ2):
                return typ1
            else:
                return FloatType()
        if ctx.op in ['%']:
            if type(typ1) is not IntegerType or type(typ2) is not IntegerType:
                raise TypeMismatchInExpression(ctx)
            return typ1

        if ctx.op in ['&&', '||']:
            if type(typ1) is not BooleanType or type(typ2) is not BooleanType:
                raise TypeMismatchInExpression(ctx)
            return typ1
        
        if ctx.op in ['::']:
            if type(typ1) is not StringType or type(typ2) is not StringType:
                raise TypeMismatchInExpression(ctx)
            return typ1
        
        if ctx.op in ['==', '!=']:
            if type(typ1) is not IntegerType and type(typ1) is not BooleanType:
                raise TypeMismatchInExpression(ctx)
            if type(typ2) is not IntegerType and type(typ2) is not BooleanType:
                raise TypeMismatchInExpression(ctx)
            return BooleanType()
        
        if ctx.op in ['>', '<', '>=', '<=']:
            if type(typ1) is not IntegerType and type(typ1) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            if type(typ2) is not IntegerType and type(typ2) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return BooleanType()
        
    def visitUnExpr(self, ctx:UnExpr, o): 
        if type(ctx.val) is ArrayLit:
            expect = ctx.val
            self.visit(ctx.val, (AutoType(),o))
            raise TypeMismatchInExpression(ctx)
        
        typ = self.visit(ctx.val, o)
        
        if ctx.op in ['-']:
            if type(typ) is AutoType:
                typ = Utils.infer(o, ctx.val.name, IntegerType())
            if type(typ) is not IntegerType and type(typ) is not FloatType:
                raise TypeMismatchInExpression(ctx)
            return typ
        
        if ctx.op in ['!']:
            if type(typ) is AutoType:
                typ = Utils.infer(o, ctx.val.name, BooleanType())
            if type(typ) is not BooleanType:
                raise TypeMismatchInExpression(ctx)
            return typ


    def visitId(self, ctx:Id, o): 
        id = Utils.checkUndeclared(Identifier(), o, ctx.name)
        return id.typ
    def visitArrayCell(self, ctx, o): 
        id = Utils.checkUndeclared(Identifier(), o, ctx.name)

        if type(id.typ) is not ArrayType:
            raise TypeMismatchInExpression(ctx)  

        for cell in ctx.cell:
            if type(cell) is ArrayType:
                self.visit(cell, (AutoType(),o))
                raise TypeMismatchInExpression(ctx) 
            
            if type(self.visit(cell, o)) is not IntegerType:
                raise TypeMismatchInExpression(ctx) 
             
        if (len(id.typ.dimensions) < len(ctx.cell)):
            raise TypeMismatchInExpression(ctx)  
        else:
            # for i in range(len(ctx.cell)):
            #     if ctx.cell[i] > id.typ.dimensions[i]:
            #         raise TypeMismatchInExpression(ctx)
            if (len(id.typ.dimensions) == len(ctx.cell)): 
                # if ctx.cell[-1] == id.typ.dimensions[-1]:
                #     raise TypeMismatchInExpression(ctx)
                # else:
                    return id.typ.typ

        return ArrayType(id.typ.dimensions[len(id.typ.dimensions)-len(ctx.cell):],id.typ.typ)
    def visitIntegerLit(self, ctx, o): 
        return IntegerType()
    def visitFloatLit(self, ctx, o): 
        return FloatType()
    def visitStringLit(self, ctx, o): 
        return StringType()
    def visitBooleanLit(self, ctx, o): 
        return BooleanType()
    def visitArrayLit(self, ctx:ArrayLit, o):
        ept, env = o

        expect = copy.deepcopy(ept)
 
        if type(expect) is ArrayType:
            if len(expect.dimensions) > 1:
                expect.dimensions = expect.dimensions[1:]
            else:
                expect = expect.typ

        typ = None
        for exp in ctx.explist:
            if type(exp) is ArrayLit:
                expTyp = self.visit(exp,(expect,env))
            else: 
                expTyp = self.visit(exp,env)
            if typ is None and type(expTyp) is not AutoType:
                typ = expTyp
                break

        for exp in ctx.explist:
            if type(exp) is ArrayLit:
                expTyp = self.visit(exp,(expect,env))
            else: 
                expTyp = self.visit(exp,env) 
            if type(expTyp) is AutoType:
                if typ is not None:
                    expTyp = Utils.infer(env, exp.name, typ)
                else:
                    expTyp = Utils.infer(env, exp.name, expect)
            

            if typ is not None and not Utils.compareType(typ, expTyp):
                raise IllegalArrayLiteral(ctx)

        if typ is None:
            typ = expect
                
        if type(typ) is not ArrayType:
            return ArrayType([len(ctx.explist)], typ)
        else:
            return ArrayType([len(ctx.explist)] + typ.dimensions, typ.typ)


    def visitFuncCall(self, ctx, o): 
        func = Utils.checkUndeclared(Function(), o, ctx.name)
        if type(func.typ) is VoidType:
            raise TypeMismatchInExpression(ctx)
        
        if len(ctx.args) == len(func.params):
            for i in range(len(ctx.args)):
                typParam = func.params[i].typ
                if type(ctx.args[i]) is ArrayLit:
                    if type(typParam) is AutoType:
                        typArgs = self.visit(ctx.args[i], (IntegerType(), o))
                    else:
                        typArgs = self.visit(ctx.args[i], (typParam, o))
                else:
                    typArgs = self.visit(ctx.args[i], o)
                
                if type(typArgs) is IntegerType and type(typParam) is FloatType:
                    continue
                if type(func.params[i].typ) is not AutoType and not Utils.compareType(typArgs, typParam):
                    raise TypeMismatchInExpression(ctx)
                if type(func.params[i].typ) is AutoType:
                    Utils.inferParam(o, ctx.name, func.params[i].name, typArgs)
                    Utils.infer(o, func.param[i].name, typArgs)

        else:
            raise TypeMismatchInExpression(ctx)
        
        return func.typ
    
    def visitIntegerType(self, ctx, o): pass
    def visitFloatType(self, ctx, o): pass
    def visitBooleanType(self, ctx, o): pass
    def visitStringType(self, ctx, o): pass
    def visitArrayType(self, ctx, o): pass
    def visitAutoType(self, ctx, o): pass
    def visitVoidType(self, ctx, o): pass





