class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = defaultdict(int)

        for i in s:
            counter[i] += 1

        freq = counter.values()
        return len(set(freq)) == 1
            