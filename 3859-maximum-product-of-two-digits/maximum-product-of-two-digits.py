class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        while(n):
            digit=n%10
            l.append(digit)
            n//=10
        s=sorted(l)
        return s[-1]*s[-2]