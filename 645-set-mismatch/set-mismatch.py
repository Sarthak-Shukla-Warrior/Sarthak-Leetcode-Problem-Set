class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        s = set(nums)
        duplicate = sum(nums) - sum(s)
        missing = sum(range(1, len(nums)+1)) - sum(s)
        return [duplicate, missing]