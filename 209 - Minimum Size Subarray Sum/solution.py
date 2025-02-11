class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left, right, addition = 0,0,0
        ans = float('inf')

        for right in range(0, len(nums)):
            addition += nums[right]

            while addition >= target:
                ans = min(ans, right - left + 1)
                addition -= nums[left]
                left += 1
     
        return ans  if ans != float('inf') else 0