class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        s1 = intervals[0][0]
        e1 = intervals[0][1]
        for i in range(len(intervals)):
            s2 = intervals[i][0]
            e2 = intervals[i][1]
            if e1 >= s2:
                s1 = s1
                e1 = max(e1,e2)
                continue
            res.append([s1,e1])
            s1 = s2
            e1 = e2
        res.append([s1,e1])
        return res
        