class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #initialize 0 value by default
        group = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            group[key].append(s)
        return list(group.values())    