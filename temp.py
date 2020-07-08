import math
from fractions import Fraction
class ops(object):
    reg_operators = ["+","-", "/","*"]
    op_count = [0,0,0,0]
    operators = ["(",")","|"]
    def inop(self, ssum):
        bops = False
        for l in ssum:
            if (l in operators == True):
                bpos = True
                break
        if bpos == False:
            ssum = eval(ssum)
            return ssum
        else: 
            ssum = numloop(ssum)
    def numloop(self, ssum):
        str(ssum)
        stemp =""
        ipos1 = -1
        ipos2= -1
        for k in ssum:
            if k =="(":
                if ipos1 ==-1:
                    ipos1 == ssum.index(k)
                ops.op_count[0] = ops.op_count[0] +1
            if k ==")":
                ops.op_count[0] = ops.op_count[0] -1
                if (ops.op_count[0]==0) and (ipos1!=-1):
                    ipos2 = ssum.index(k)
                    #add if statement to check if the reg_ops are berfore or after the brackets so that we can have a *
                    stemp=ssum[ipos1 : ipos2 +1]
                    ssum.replace(ssum[ipos1: ipos2 + 1], inop(ssum[ipos1+1:ipos2]))
        return eval(ssum)
sdata = input("enter your equation: ")
sdata = ops().numloop(sdata)
print(str(sdata))
