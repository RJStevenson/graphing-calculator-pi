import math
from fractions import Fraction
def check_str_contains_list(ssen,slist):
    bhas = False
    ssen = str(ssen)
    slist = list(slist)
    for k in ssen:
        if k in slist:
            bhas =  True
            break
    return bhas
class formulas(object):
    def plus(self, fuck):
        fuck = list(fuck)
        symbol = "+"
        lnum = str(fuck[0])
        rnum = str(fuck[1])
        x = ops().check_for_ops(lnum, rnum, "+")
        return x[0] + x[1]
    def minus(self, fuck):
        fuck = list(fuck)
        symbol = "-"
        lnum = str(fuck[0])
        rnum = str(fuck[1])
        x = ops().check_for_ops(lnum, rnum, "+")
        return x[0] - x[1]

    def multi(self, fuck):
        fuck = list(fuck)
        symbol = "-"
        lnum = str(fuck[0])
        rnum = str(fuck[1])
        x = ops().check_for_ops(lnum, rnum, "+")
        return x[0] * x[1]

    def div(self, fuck):
        fuck = list(fuck)
        symbol = "-"
        lnum = str(fuck[0])
        rnum = str(fuck[1])
        x = ops().check_for_ops(lnum, rnum, "+")
        return x[0] / x[1]


class ops(object):  #checking for the signs +-/abs etc
    def check_for_ops(self, lnum, rnum, ssign): # for equations that have different side for example plus minus divide
        if (check_str_contains_list(lnum, ops().lreserv()) == False) and (check_str_contains_list(rnum, ops().lreserv()) == False):
            return [float(lnum),float(rnum)]
        else:
                if (check_str_contains_list(lnum, ops().lreserv()) == True):
                    lnum = ops().numloop(lnum)
                if (check_str_contains_list(rnum, ops().lreserv()) == True):
                    rnum = ops().numloop(lnum)
                return [float(lnum), float(rnum)]

    def lreserv(self):
        x = ["x", "y", "/", "+", "-", "*"]
        return x
    

    def numloop(self, ssum):
        def sides(ipos,ssum):
            leftside = ssum[0:ipos]
            rightside= ssum[ipos+1: len(ssum)]
            return [leftside, rightside]
        def switch(op_char, ipos, ssum):
            if(op_char=="*"):
                return formulas().multi(sides(ipos, ssum))
            elif (op_char == "/"):
                return formulas().div(sides(ipos, ssum))
            elif(op_char == "+"):
                return formulas().plus(sides(ipos,ssum))
            elif (op_char == "-"):
                return formulas().minus(sides(ipos, ssum))

        for k in ssum:
            if check_str_contains_list(ssum, ops().lreserv())==False:
                break
            if k in ops().lreserv():
                  ssum = switch(k, ssum.index(k), ssum)
        return ssum
sdata = input("enter your some")

if sdata.capitalize() != "FRAC":
    x = ops().numloop(sdata)
    x = float(x)
    x =Fraction(x).limit_denominator(10000000)
    print((x))
elif sdata.capitalize() == "FRAC":
    print(float(x))
