class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        l=[]
        for i in range(1,n+1):
            if(n%i==0):
                l.append(nums[i-1])
                
        return sum(i**2 for i in l)