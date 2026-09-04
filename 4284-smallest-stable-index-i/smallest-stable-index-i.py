class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(0,len(nums)):
            if i==0:
                a=nums[0]
                b=min(nums[i:len(nums)])
            else:
                a=max(nums[0:i])
                b=min(nums[i:len(nums)])

            if (a-b) <= k:
                return i
        else:
            return -1