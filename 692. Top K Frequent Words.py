class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cntr = Counter(words)
        res = sorted(cntr, key = lambda x: (-cntr[x], x))
        return res[:k]