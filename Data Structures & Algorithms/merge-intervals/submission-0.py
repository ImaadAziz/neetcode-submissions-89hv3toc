class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])

        output = [intervals[0]]
        for s, e in intervals:
            endTime = output[-1][1]
            if s <= endTime:
                output[-1][1] = max(e, endTime)
            else:
                output.append([s,e])

        return output