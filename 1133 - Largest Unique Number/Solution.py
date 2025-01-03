from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        result = [-1]
        for key, value in count.items():
            if value == 1:
                result.append(key)
        return(max(result))