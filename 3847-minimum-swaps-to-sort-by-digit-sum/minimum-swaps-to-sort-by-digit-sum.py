class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            return sum(int(d) for d in str(x))

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        index_map = {num: i for i, num in enumerate(sorted_nums)}

        visited = set()
        swaps = 0

        for i, num in enumerate(nums):
            if i in visited or index_map[num] == i:
                continue
            cycle_size, j = 0, i
            while j not in visited:
                visited.add(j)
                j = index_map[nums[j]]
                cycle_size += 1
            swaps += cycle_size - 1
        return swaps