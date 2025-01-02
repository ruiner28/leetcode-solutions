class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            for j in i:
                count[j] += 1
        
        ans= []

        n = len(nums)
        for i in count:
            if count[i] == n:
                ans.append(i)
        return(sorted(ans))        