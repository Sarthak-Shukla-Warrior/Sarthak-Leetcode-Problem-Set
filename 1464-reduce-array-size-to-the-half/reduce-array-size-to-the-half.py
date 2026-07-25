class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)             
        counts = sorted(freq.values(), reverse=True)  
        removed = 0
        total = 0
        half = len(arr) // 2
        
        for c in counts:
            total += c
            removed += 1
            if total >= half:
                return removed