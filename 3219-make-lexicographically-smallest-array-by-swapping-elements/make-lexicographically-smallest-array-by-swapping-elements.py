class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ans = [0] * len(nums)
        num_and_idx = sorted([(num, i) for i, num in enumerate(nums)])
        
        groups = []
        for num, idx in num_and_idx:
            if not groups or num - groups[-1][-1][0] > limit:
                groups.append([(num, idx)])
            else:
                groups[-1].append((num, idx))
        
        for group in groups:
            sorted_nums = [num for num, _ in group]
            sorted_indices = sorted([idx for _, idx in group])
            for i in range(len(group)):
                ans[sorted_indices[i]] = sorted_nums[i]
        
        return ans