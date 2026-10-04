class Solution:
    import math
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        l=[]
        for i in range(1,math.ceil(num**0.5)+1):
            if num%i==0:
                l.append(i)
                if (i != num // i) and (num // i != num):  
                        l.append(num // i)

        return sum(set(l))==num