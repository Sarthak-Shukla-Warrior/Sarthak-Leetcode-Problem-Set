class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, start=1):  
            pos = ord(ch) - ord('a') + 1     
            rev_val = 27 - pos               
            total += rev_val * i
        return total