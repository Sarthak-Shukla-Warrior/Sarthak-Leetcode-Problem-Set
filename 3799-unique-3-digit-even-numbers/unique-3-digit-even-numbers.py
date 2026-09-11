class Solution:
    from collections import Counter
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = Counter(digits)
        ans = []
        for num in range(100, 1000, 2):  
            cnt_num = Counter(map(int, str(num)))
            if all(cnt[d] >= cnt_num[d] for d in cnt_num):
                ans.append(num)
        return len(ans)