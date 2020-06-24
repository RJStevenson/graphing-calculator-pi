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
        x = ops().check_for_ops(lnum, rnum, "")
        return x[0] + x[1]
    def minus(self, fuck):
        fuck = list(fuck)
        symbol = "-"
        lnum = str(fuck[0])
        rnum = str(fuck[1])
        x = ops().check_for_ops(lnum, rnum, "")
        return x[0] - x[1]

    def multi(self, fuck):
        fuck = list(fuck)
        symbol = "-"
        lnum = str(fuck[0])
        rnum = str(fuck[1])
        x = ops().check_for_ops(lnum, rnum, "")
        return x[0] * x[1]

    def div(self, fuck):
        fuck = list(fuck)
        symbol = "-"
        lnum = str(fuck[0])
        rnum = str(fuck[1])
        x = ops().check_for_ops(lnum, rnum, "")
        return x[0] / x[1]
    
    def abs(self,fuck):
        fuck = list(fuck)
        symbol = "|"
        lnum = str(fuck[0])
        rnum = str(fuck[1])
        inum = str(fuck[2])
        x = ops().check_for_ops(lnum,rnum,inum)
        x[2] = str(math.fabs(x[2]))
        mysep =""
        return  float(mysep.join(x))


class ops(object):  #checking for the signs +-/abs etc
    def check_for_ops(self, lnum, rnum, ssign): # for equations that have different side for example plus minus divide
        if(len(lnum) == 0):
            lnum = 0
        if(len(ssign)==0):
                
            if (check_str_contains_list(lnum, ops().lreserv()) == False) and (check_str_contains_list(rnum, ops().lreserv()) == False):
                return [float(lnum),float(rnum)]
            else:
                    if (check_str_contains_list(lnum, ops().lreserv()) == True):
                        lnum = ops().numloop(lnum)
                    if (check_str_contains_list(rnum, ops().lreserv()) == True):
                        rnum = ops().numloop(rnum)
                    return [float(lnum), float(rnum)]
        else:
            if (check_str_contains_list(lnum, ops().lreserv()) == False) and (check_str_contains_list(rnum, ops().lreserv()) == False) and (check_str_contains_list(ssign, ops().lreserv()) == False):
                return [str(lnum), str(rnum),float(ssign)]
            else:
                    if (check_str_contains_list(lnum, ops().lreserv()) == True):
                        lnum = ops().numloop(lnum)
                    if (check_str_contains_list(rnum, ops().lreserv()) == True):
                        rnum = ops().numloop(rnum)
                    if (check_str_contains_list(ssign, ops().lreserv()) == True) :
                        ssign = ops().numloop(ssign)
                    return [float(lnum), float(rnum), float(ssign)]

    def lreserv(self):
        x = ["x", "y", "/", "+", "-", "*","|"]
        return x
    

    def numloop(self, ssum):
        def sides(ipos,ssum): # for side operators like + - divide
            leftside = ssum[0:ipos]
            rightside= ssum[ipos+1: len(ssum)]
            return [leftside, rightside]

             
        def inop(ipos1, ipos2,ssum): # for inoperators such as sin cos || ln log
            leftside = ssum[0:ipos1]
            inside = ssum[ipos1+1:ipos2]
            rightside = ssum[ipos2+1:len(ssum)]
            return [leftside,rightside,inside]
        def switch(op_char, ipos, ssum):
            ssum = str(ssum)
            if(op_char=="*"):
                return formulas().multi(sides(ipos, ssum))
            elif (op_char == "/"):
                return formulas().div(sides(ipos, ssum))
            elif(op_char == "+"):
                return formulas().plus(sides(ipos,ssum))
            elif (op_char == "-"):
                return formulas().minus(sides(ipos, ssum))
            elif (op_char =="|"):
                return formulas().abs(inop(ipos,ssum.find(op_char,ipos+1,len(ssum)),ssum))

        for k in ssum:
            if check_str_contains_list(ssum, ops().lreserv())==False:
                break
            if k in ops().lreserv():
                  ssum = switch(k, ssum.index(k), ssum)
        return ssum
t = True
while t == True:
    mem = open("mem.txt")
    sfile = mem.read()
    mem.close()
    mem = open("mem.txt","r")
    fline = mem.readline()
    mem.close()
    sdata = input("enter your some")
    if sdata == "":
        break
    elif sdata.upper() == "EXIT":
        t= False
        break
    elif (sdata.upper()) != "FRAC":
            mem = open ("mem.txt","w")
            x = ops().numloop(sdata)
            x = float(x)
            mem.write(str(x)+ "\n" + sfile)
            print(str(x))
    elif sdata.upper() == "FRAC":
            x = float(fline)
            x =Fraction(x).limit_denominator(10000000)
            print((x))
