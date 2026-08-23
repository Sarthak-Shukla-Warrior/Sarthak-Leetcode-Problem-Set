class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sumL = sum(int(c) for c in num[:half] if c.isdigit())
        sumR = sum(int(c) for c in num[half:] if c.isdigit())
        
        qL = sum(1 for c in num[:half] if c == '?')
        qR = sum(1 for c in num[half:] if c == '?')
 
        if (qL + qR) % 2 == 1:
            return True
        
        return (sumL - sumR) * 2 != 9 * (qR - qL)