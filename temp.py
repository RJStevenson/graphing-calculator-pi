import math
from fractions import Fraction 
class rit:
    def __init__(self, ssum, ipos1):
        self.ssum = str(ssum)
        self.ipos1 = int(ipos1)
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
    trig = ['cosh','tanh','sinh','cos','sin','tan','abs']


    def numloop(self, ssum):
        ops.op_count[0] = 0
        
        def inop(self,ssum,ipos1):
            ops.op_count[0] = 1
            while ops.op_count[0] != 0:
                if ssum[ipos1] == ")":
                    ops.op_count[0] = ops.op_count[0] -1
                elif ssum[ipos1] == "(":
                    ops.op_count[0] = ops.op_count[0] + 1
                if ops.op_count[0]!=0:    
                    ipos1 = ipos1+1
            ssum= ops.numloop.trig(ssum[0:ipos1])
            ssum = ops.numloop.brac_remove(ssum)
            return [ssum,ipos1]
                
        def trig(self,ssum):
            stemp = ""
         for k in ops.trig:
             while k in ssum:
                 ipos1 = ops().find_nth(ssum,k,1)
                 if ssum[ssum.index(k)+1] !='(':
                     return "not bracket in after " + k
                     exit
                 if k == 'cos':
                        srit = (ops.numloop.inop(ssum[ipos1 +1:len(ssum)-1],ipos1+1))
                        stemp = srit[0]
                        ipos2 = srit[2]
                        stemp = str(math.cos(stemp))
                        ssum = ssum[0:ipos1] + stemp + ssum[stemp[1]:len(ssum)-1]
         return ssum
        def brac_remove(self, ssum):
            ops.op_count[0] = 0
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
