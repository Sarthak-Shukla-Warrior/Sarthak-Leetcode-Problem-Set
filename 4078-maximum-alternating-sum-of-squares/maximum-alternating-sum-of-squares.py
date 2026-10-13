class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [x * x for x in nums]
        
        nums.sort()
        
        n = len(nums)
        m = n >> 1  
        
        ans = 0
        for i, x in enumerate(nums):
            if i < m:
                ans -= x  
            else:
                ans += x  
        return ans

        