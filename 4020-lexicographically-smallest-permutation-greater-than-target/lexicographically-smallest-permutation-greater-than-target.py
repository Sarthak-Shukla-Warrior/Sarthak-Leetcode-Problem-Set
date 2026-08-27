class Solution:
    from collections import Counter
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)

        def build(prefix, idx):
            if idx == n:
                return prefix if prefix > target else ""
          
            ch = target[idx]
            if count[ch] > 0:
                count[ch] -= 1
                res = build(prefix + ch, idx + 1)
                if res: 
                    return res
                count[ch] += 1 
 
            for c in sorted(count.keys()):
                if count[c] > 0 and c > ch:
                    count[c] -= 1
                    suffix = []
                    for k in sorted(count.keys()):
                        suffix.extend([k] * count[k])
                    return prefix + c + "".join(suffix)
            return ""

        return build("", 0)