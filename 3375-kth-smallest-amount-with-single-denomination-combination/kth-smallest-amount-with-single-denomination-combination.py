class Solution:
    from math import gcd
    from typing import List
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)

        def count(x):
            n = len(coins)
            total = 0
            for mask in range(1, 1 << n):
                l = 1
                bits = 0
                for i in range(n):
                    if mask >> i & 1:
                        l = lcm(l, coins[i])
                        bits += 1
                if bits % 2 == 1:
                    total += x // l
                else:
                    total -= x // l
            return total

        left, right = 1, k * min(coins)
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left