class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        cntr1 = Counter(s1)
        cntr2 = Counter(s2[:window])

        if cntr1 == cntr2:
            return True

        for i in range(1, len(s2) - window + 1):
            cntr2[s2[i + window - 1]] += 1
            cntr2[s2[i - 1]] -= 1
            if cntr2[s2[i - 1]] == 0:
                del cntr2[s2[i - 1]]
            if cntr2 == cntr1:
                return True
        return False
