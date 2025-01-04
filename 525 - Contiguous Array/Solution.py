class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total = 0
        d = {}
        d[0] = -1
        max_len = 0
        for i in range(len(nums)):
            total += 1 if nums[i] else -1
            if total in d:
                max_len = max(max_len, i - d[total])
            else:
                d[total] = i
        return max_len