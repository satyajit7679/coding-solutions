class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        insert = False

        for i in range(len(intervals)):
            s2 = intervals[i][0]
            e2 = intervals[i][1]

            if newInterval[0] < s2:
                if insert == False:
                    res.append(newInterval)
                    insert = True
                res.append(intervals[i])
            else:
                res.append(intervals[i])

        if insert == False:
            res.append(newInterval)

        return self.merge_interval(res)

    def merge_interval(self, arr):
        s1 = arr[0][0]
        e1 = arr[0][1]
        res = []

        for i in range(1, len(arr)):
            s2 = arr[i][0]
            e2 = arr[i][1]

            if e1 >= s2:
                s1 = s1
                e1 = max(e1, e2)
                continue

            res.append([s1, e1])
            s1 = s2
            e1 = e2

        res.append([s1, e1])
        return res