from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indexes = []
        cntr1 = Counter(p)
        window = len(p)
        cntr2 = Counter(s[:window])

        if cntr1==cntr2:
            indexes.append(0)
        for i in range(1, len(s) - window + 1):
            cntr2[s[window + i - 1]] += 1
            cntr2[s[i-1]] -= 1
            if cntr2[s[i-1]] == 0:
                del cntr2[s[i-1]]
            if cntr1==cntr2:
                indexes.append(i)
        return indexes
