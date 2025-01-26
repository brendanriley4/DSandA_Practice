class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(intervals) == 0:
            return [[]]
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        myIntervals = []
        print(f"{len(intervals)}, {intervals}")
        i = 1
        start = intervals[0][0]
        end = intervals[0][1]
        while i < len(intervals):
            if end >= intervals[i][0]:
                if end <= intervals[i][1]:
                    end = intervals[i][1]
                i += 1
            else:
                myIntervals.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
                i += 1
        myIntervals.append([start, end])
        return myIntervals


if __name__ == "__main__":
    intervals = [[1, 4], [2, 3]]
    solution = Solution()

    merged_intervals = solution.merge(intervals)
    print("Merged intervals:", merged_intervals)