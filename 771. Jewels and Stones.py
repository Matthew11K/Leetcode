class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        uniq = set(jewels)
        cnt = 0
        for s in stones:
            if s in uniq:
                cnt +=1
        return cnt