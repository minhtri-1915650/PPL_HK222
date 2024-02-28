from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):

    # Visit a parse tree produced by MT22Parser#program.
    # program: decls EOF;
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))

    # Visit a parse tree produced by MT22Parser#decls.
    # decls: decl decls | decl;
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decls())

    # Visit a parse tree produced by MT22Parser#decl.
    # decl: vardecl | fundecl;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return [self.visit(ctx.fundecl())]

    # Visit a parse tree produced by MT22Parser#vardecl.
    # vardecl: shortform | initial;
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#shortform.
    # shortform: idlist CL vartype SEMI;
    def visitShortform(self, ctx:MT22Parser.ShortformContext):
        typ = self.visit(ctx.vartype())
        return list(map(lambda x: VarDecl(x, typ), self.visit(ctx.idlist())))

    # Visit a parse tree produced by MT22Parser#idlist.
    # idlist: ID CM idlist | ID;
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())

    # Visit a parse tree produced by MT22Parser#vartype.
    # vartype: atomictype | arraytype | AUTO;
    def visitVartype(self, ctx:MT22Parser.VartypeContext):
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#initial.
    # initial: ID initialbody expr SEMI;
    def visitInitial(self, ctx:MT22Parser.InitialContext):
        initialbody = self.visit(ctx.initialbody())
        name = [ctx.ID().getText()] + initialbody[0]
        init = initialbody[2] + [self.visit(ctx.expr())]
        typ = initialbody[1]

        return list(map(lambda x, y: VarDecl(x, typ, y), name, init))

    # Visit a parse tree produced by MT22Parser#initialbody.
    # initialbody: CM ID initialbody expr CM | CL vartype ASSIGN;
    def visitInitialbody(self, ctx:MT22Parser.InitialbodyContext):
        if ctx.vartype():
            return [[], self.visit(ctx.vartype()), []]

        initialbody = self.visit(ctx.initialbody())
        name = [ctx.ID().getText()] + initialbody[0]
        init = initialbody[2] + [self.visit(ctx.expr())]
        typ = initialbody[1]
        return [name, typ, init]

    # Visit a parse tree produced by MT22Parser#fundecl.
    # fundecl: ID CL FUNCTION funtype LB paramlist RB isinherit body;
    def visitFundecl(self, ctx:MT22Parser.FundeclContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.funtype())
        params = self.visit(ctx.paramlist())
        inherit = self.visit(ctx.isinherit())
        body = self.visit(ctx.body())
        return FuncDecl(name, typ, params, inherit, body)

    # Visit a parse tree produced by MT22Parser#funtype.
    # funtype: vartype | VOID;
    def visitFuntype(self, ctx:MT22Parser.FuntypeContext):
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.vartype())

    # Visit a parse tree produced by MT22Parser#paramlist.
    # paramlist: params |; 
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.params())

    # Visit a parse tree produced by MT22Parser#params.
    # params: param CM params | param; 
    def visitParams(self, ctx:MT22Parser.ParamsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.params())

    # Visit a parse tree produced by MT22Parser#param.
    # param: INHERIT? OUT? ID CL vartype;
    def visitParam(self, ctx:MT22Parser.ParamContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.vartype())
        out  = ctx.OUT() is not None
        inherit = ctx.INHERIT() is not None
        return ParamDecl(name, typ, out, inherit)

    # Visit a parse tree produced by MT22Parser#isinherit.
    # isinherit: INHERIT ID |;
    def visitIsinherit(self, ctx:MT22Parser.IsinheritContext):
        return ctx.ID().getText() if ctx.ID() else None

    # Visit a parse tree produced by MT22Parser#body.
    # body: blockstmt;
    def visitBody(self, ctx:MT22Parser.BodyContext):
        return self.visit(ctx.blockstmt())

    # Visit a parse tree produced by MT22Parser#blockstmt.
    # blockstmt: LCP blockbody RCP;
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return BlockStmt(self.visit(ctx.blockbody()))

    # Visit a parse tree produced by MT22Parser#blockbody.
    # blockbody: stmtlist blockbody | ;
    def visitBlockbody(self, ctx:MT22Parser.BlockbodyContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmtlist()) + self.visit(ctx.blockbody())

    # Visit a parse tree produced by MT22Parser#stmtlist.
    # stmtlist: stmt | vardecl;
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())]
        return self.visit(ctx.vardecl())

    # Visit a parse tree produced by MT22Parser#stmt.
    # stmt: assignstmt | ifstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | returnstmt | callstmt | blockstmt;
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#assignstmt.
    # assignstmt: lhs ASSIGN expr SEMI;
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    # Visit a parse tree produced by MT22Parser#lhs.
    # lhs: ID | indexop;
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.indexop())

    # Visit a parse tree produced by MT22Parser#ifstmt.
    # ifstmt: matchstmt | unmatchstmt;
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#matchstmt.
    # matchstmt: IF LB expr RB matchstmt ELSE matchstmt | other;
    def visitMatchstmt(self, ctx:MT22Parser.MatchstmtContext):
        if ctx.other():
            return self.visit(ctx.other())
        return IfStmt(self.visit(ctx.expr()),  self.visit(ctx.matchstmt(0)), self.visit(ctx.matchstmt(1)))

    # Visit a parse tree produced by MT22Parser#other.
    # other: assignstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | returnstmt | callstmt | blockstmt;
    def visitOther(self, ctx:MT22Parser.OtherContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#unmatchstmt.
    # unmatchstmt: IF LB expr RB ifstmt | IF LB expr RB matchstmt ELSE unmatchstmt;
    def visitUnmatchstmt(self, ctx:MT22Parser.UnmatchstmtContext):
        cond = self.visit(ctx.expr())
        if ctx.ELSE():
            return IfStmt(cond, self.visit(ctx.matchstmt()), self.visit(ctx.unmatchstmt()))
        return IfStmt(cond, self.visit(ctx.ifstmt()))

    # Visit a parse tree produced by MT22Parser#forstmt.
    # forstmt: FOR LB lhs ASSIGN expr CM expr CM expr RB stmt;
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        init = AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr(0)))
        cond = self.visit(ctx.expr(1))
        upd = self.visit(ctx.expr(2))
        stmt = self.visit(ctx.stmt())
        return ForStmt(init, cond, upd, stmt)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    # whilestmt: WHILE LB expr RB stmt;
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(cond, stmt)

    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    # dowhilestmt: DO blockstmt WHILE LB expr RB SEMI;
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        cond = self.visit(ctx.expr())
        stmt = self.visit(ctx.blockstmt())
        return DoWhileStmt(cond, stmt)

    # Visit a parse tree produced by MT22Parser#breakstmt.
    # breakstmt: BREAK SEMI;
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return BreakStmt()

    # Visit a parse tree produced by MT22Parser#continuestmt.
    # continuestmt: CONTINUE SEMI;
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return ContinueStmt()

    # Visit a parse tree produced by MT22Parser#returnstmt.
    # returnstmt: RETURN expr? SEMI;
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()

    # Visit a parse tree produced by MT22Parser#callstmt.
    # callstmt: funcall SEMI;
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        funcall = self.visit(ctx.funcall())
        return CallStmt(funcall.name, funcall.args)

    # Visit a parse tree produced by MT22Parser#atomictype.
    # atomictype: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomictype(self, ctx:MT22Parser.AtomictypeContext):
        if ctx.BOOLEAN():
            return BooleanType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()

    # Visit a parse tree produced by MT22Parser#arraytype.
    # arraytype: ARRAY LSP dimensions RSP OF atomictype;
    def visitArraytype(self, ctx:MT22Parser.ArraytypeContext):
        return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.atomictype()))

    # Visit a parse tree produced by MT22Parser#dimensions.
    # dimensions: INTLIT CM dimensions | INTLIT;
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimensions())

    # Visit a parse tree produced by MT22Parser#expr.
    # expr: expr1 CONC expr1 | expr1;
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        return BinExpr(op, left, right)

    # Visit a parse tree produced by MT22Parser#expr1.
    # expr1: expr2 EQUAL expr2 | expr2 NEQUAL expr2 | expr2 SMALL expr2 | expr2 LARGE expr2| expr2 SMALLEQ expr2 | expr2 LARGEEQ expr2 | expr2;
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        return BinExpr(op, left, right)

    # Visit a parse tree produced by MT22Parser#expr2.
    # expr2: expr2 AND expr3 | expr2 OR expr3 | expr3;
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        return BinExpr(op, left, right)

    # Visit a parse tree produced by MT22Parser#expr3.
    # expr3: expr3 ADDOP expr4 | expr3 SUBOP expr4 | expr4;
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        return BinExpr(op, left, right)

    # Visit a parse tree produced by MT22Parser#expr4.
    # expr4: expr4 MULOP expr5 | expr4 DIVOP expr5 | expr4 MODOP expr5 | expr5;
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()
        return BinExpr(op, left, right)

    # Visit a parse tree produced by MT22Parser#expr5.
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        val = self.visit(ctx.getChild(1))
        op = ctx.getChild(0).getText() 
        return UnExpr(op, val)

    # Visit a parse tree produced by MT22Parser#expr6.
    # expr6: SUBOP expr6 | expr7;
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        val = self.visit(ctx.getChild(1))
        op = ctx.getChild(0).getText() 
        return UnExpr(op, val)

    # Visit a parse tree produced by MT22Parser#expr7.
    # expr7: ID | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | indexop | funcall | arraylit | LB expr RB;
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            val = ctx.FLOATLIT().getText()
            if (val[0] == '.'): val = '0' + val
            return FloatLit(float(val))
        elif ctx.BOOLLIT():
            return BooleanLit(ctx.BOOLLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by MT22Parser#indexop.
    # indexop: ID LSP exprs RSP;
    def visitIndexop(self, ctx:MT22Parser.IndexopContext):
        name = ctx.ID().getText()
        cell = self.visit(ctx.exprs())
        return ArrayCell(name, cell)

    # Visit a parse tree produced by MT22Parser#funcall.
    # funcall: ID LB exprlist RB;
    def visitFuncall(self, ctx:MT22Parser.FuncallContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.exprlist())
        return FuncCall(name, args)

    # Visit a parse tree produced by MT22Parser#exprlist.
    # exprlist: exprs |;
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.exprs())

    # Visit a parse tree produced by MT22Parser#exprs.
    # exprs: expr CM exprs | expr;
    def visitExprs(self, ctx:MT22Parser.ExprsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprs())

    # Visit a parse tree produced by MT22Parser#arraylit.
    # arraylit: LCP exprlist RCP;
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()))
    