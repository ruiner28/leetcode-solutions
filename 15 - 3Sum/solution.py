class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []    
        nums.sort()
        n = len(nums)

        for x in range(n - 2):
            if x > 0 and nums[x] == nums[x- 1]:
                continue

            y, r = x+1, n-1

            while y < r:
                total = nums[x] + nums[y] + nums[r]            

                if total == 0:
                    ans.append([nums[x],nums[y], nums[r]])
                    y += 1
                    r -= 1

                    while y < r and nums[y] == nums[y - 1]:
                        y += 1
                    while y < r and nums[r] == nums[r + 1]:
                        r -= 1    

                elif total < 0:
                    y += 1
                else:
                    r -= 1
        return ans                    