class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []

        minimum = intervals[0][0]
        maximum = intervals[0][1]

        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]

            if start <= maximum:
                maximum = max(maximum, end)
            else:
                result.append([minimum, maximum])

                minimum = start
                maximum = end

        result.append([minimum, maximum])

        return result