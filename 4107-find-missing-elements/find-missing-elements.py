class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min1=min(nums)
        max1=max(nums)
        s=set(nums)
        missing=[]
        for num in range(min1,max1+1):
            if num not in s:
                missing.append(num)
        return missing