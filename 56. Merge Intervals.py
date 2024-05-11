class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        nel = len(intervals)
        cur_interval = intervals[0]
        for i in range(1,nel):
            if cur_interval[1]>=intervals[i][0]:
                cur_interval[1]=max(intervals[i][1],cur_interval[1])
            else:
                res.append(cur_interval)
                cur_interval = intervals[i]
        res.append(cur_interval)
        return res