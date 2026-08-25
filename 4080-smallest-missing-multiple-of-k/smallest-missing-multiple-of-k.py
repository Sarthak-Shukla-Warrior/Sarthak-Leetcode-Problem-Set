class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while True:
            if i%k==0 and i not in nums:
                return i
            i+=1