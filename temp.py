import math
from fractions import Fraction 
class ops(object):
    def find_nth(self, haystack, needle, n):
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start
    reg_operators = ["+","-", "/","*"] #regonized operators by the function eval
    op_count = [0,0,0,0] #array to count the occurences of the operators the array below
    operators = ["(",")","|"] #operators that program looks for
    brac_occurence = []
    '''
    def inop(self, ssum):
        bops = False
        for l in ssum:
            if l == "(":
                ops().op_count[0] = ops().op_count[0] +1
            if l == ")":
                ops().op_count[1] = ops().op_count[1] + 1
            if (l in ops().operators == True):
                bpos = True
        if ops.op_count[0] != ops.op_count[1]:
            return "incorrect brackets"
        elif bpos == False:
            ssum = eval(ssum)
            return ssum
        else: 
            ops.op_count[0] = 0
            ssum = numloop(ssum)
            return ssum
    '''

    def numloop(self, ssum):
        str(ssum)
        for k in ssum:
            if k == "(":
                ops.op_count[0] = ops.op_count[0] +1
            if k == ")":
                ipos1 = ops().find_nth(ssum,"(", ops.op_count[0])
                ipos2 = ssum.index(k)
                stemp = ssum[ipos1+1: ipos2]
                stemp = str(ops().numloop(stemp))
                if ipos1 != 0 and ipos2!= len(ssum)-1:
                    if (ssum[ipos1 - 1] in ops.reg_operators):
                            ssum = ssum[0:ipos1] + stemp + ssum[ipos2+1:len(ssum)]
                    if (ssum[ipos1 - 1] not in ops.reg_operators):
                        ssum = ssum[0:ipos1] + '*'  + stemp  +ssum[ipos2+1:len(ssum)]
                else:
                    if (ipos1 == 0) and (ipos2==len(ssum)-1):
                       ssum =  stemp
                    elif(ipos1!=0) and (ipos2==len(ssum)-1):
                         if(ssum[ipos1-1] not in ops.reg_operators):
                                ssum = ssum[0:ipos1] + '*' + stemp
                         else: 
                             ssum = ssum[0:ipos1]  + stemp
                    elif(ipos1==0)and(ipos2!=len(ssum)-1):
                            ssum = stemp + ssum[ipos2+1:len(ssum)]

                ops.op_count[0] = ops.op_count[0] -1
        return eval(ssum)
sdata = input("enter your equation: ") #getting the equation from user
sdata = str(sdata).replace(" ", "")#removing any white space
sdata = ops().numloop(sdata)
print(str(sdata))#printing solution
