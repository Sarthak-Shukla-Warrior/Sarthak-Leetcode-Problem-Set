class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        left = 0
        count = 0

        for right in range(n):
            if s[right] == '1':
                count += 1

            # When we have k ones, try to shrink from left
            while count == k:
                candidate = s[left:right+1]
                if not ans or len(candidate) < len(ans) or (len(candidate) == len(ans) and candidate < ans):
                    ans = candidate

                if s[left] == '1':
                    count -= 1
                left += 1

        return ans