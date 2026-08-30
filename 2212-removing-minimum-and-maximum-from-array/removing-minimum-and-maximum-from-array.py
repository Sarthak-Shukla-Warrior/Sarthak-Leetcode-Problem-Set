class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mi = mx = 0
        n = len(nums)
        
        for i, num in enumerate(nums):
            if num < nums[mi]:
                mi = i
            if num > nums[mx]:
                mx = i
        
        if mi > mx:
            mi, mx = mx, mi
        
        return min(mx + 1, n - mi, mi + 1 + n - mx)
   