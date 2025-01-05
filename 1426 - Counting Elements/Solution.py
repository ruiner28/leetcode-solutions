from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        total = 0
        c = Counter(arr)
        for key, val in c.items():
            if (key+1) in c:
                total += val
        return total