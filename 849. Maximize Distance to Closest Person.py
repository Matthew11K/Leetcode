class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, prev, dist = 0, -1, 0
        for i,n in enumerate(seats):
            if n:
                if prev == -1:
                    dist = i
                else:
                    dist = (i-prev)//2
                res = max(res, dist)
                prev = i
        if not seats[-1]:
            res = max(res, i - prev)
        return res