# Solution 1
class Solution:
    def merge(intervals):
        """Returns an array of non-overlapping intervals.
        
        Source: https://leetcode.com/problems/merge-intervals/
        """
        
        # pointers to keep track of intervals being checked
        first, second = 0, 1
        # sort the intervals
        intervals.sort()
        
        while second < len(intervals):
            if  intervals[second][0] < intervals[first][0]:
                secInterval = intervals.pop(second)
                intervals[first][0] = secInterval[0]
                if  secInterval[1] > intervals[first][1]:
                    intervals[first][1] = secInterval[1]
            elif intervals[second][0] <= intervals[first][1]:
                secInterval = intervals.pop(second)
                if secInterval[1] > intervals[first][1]:
                    intervals[first][1] = secInterval[1]
            else:
                first += 1
                second += 1
                
        return intervals

# Solution 2:
# Source: https://leetcode.com/problems/merge-intervals/solution/
class Solution:
    def merge(intervals):

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged