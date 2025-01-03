class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hash_map = defaultdict(int)

        for win, loss in matches:
            hash_map[loss] += 1
            hash_map[win] = hash_map[win]

        winner = [key for key, value in hash_map.items() if value == 0]
        losses = [key for key, value in hash_map.items() if value ==1]    
        return [sorted(winner), sorted(losses)]