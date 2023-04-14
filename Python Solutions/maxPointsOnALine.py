"""

# Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.

# Source: https://leetcode.com/problems/max-points-on-a-line/

# Intuition
> We need to find the maximum number of points that lie on the same straight line. We can achieve this by computing the slope between every pair of points and checking which of the slopes occur the most frequently.


# Approach
> We can iterate over every pair of points and compute their slope. We store the count of each slope in a dictionary. We also store the count of same points in a variable same_points.

> After iterating over all pairs of points, we check whether the dictionary of slopes is empty or not. If it is empty, it means all points are the same and we return the count of same points. Otherwise, we iterate over the dictionary of slopes and compute the maximum number of points that lie on the same line for each slope. We add the number of same points to this count and keep track of the maximum value we have seen so far.

> Finally, we return the maximum value we have seen so far.

# Complexity
- Time complexity:
> `O(n^2)`, where n is the number of points in the input list. We need to iterate over every pair of points to compute their slopes.

- Space complexity:
> `O(n)`, for storing the dictionary of slopes. In the worst case, all the points can be unique, so we would need to store n-1 slopes.

# Code
"""


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n < 2:
            return n

        max_points = 0
        for i in range(n):
            slopes = {}
            same_points = 1

            for j in range(i + 1, n):
                if points[i] == points[j]:
                    same_points += 1
                else:
                    slope = (
                        float("inf")
                        if points[i][0] == points[j][0]
                        else (points[i][1] - points[j][1])
                        / (points[i][0] - points[j][0])
                    )
                    slopes[slope] = slopes.get(slope, 0) + 1

            if not slopes:
                max_points = max(max_points, same_points)
            else:
                for slope, count in slopes.items():
                    max_points = max(max_points, count + same_points)

        return max_points
