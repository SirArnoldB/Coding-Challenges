# K Closest Points to Origin

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


# Example 1:

# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]

# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.


# Constraints:

# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104

# Solution: Heap
from heapq import heappop, heappush
from typing import List


class Solution:
    def distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # keepa track of the k closest points
        candidate_points = []
        # add the point at index to the closest points
        # we negate the distance so that the point at the top will have the
        # largest distance from the origin
        heappush(candidate_points, [-self.distance(points[0]), points[0]])

        for idx in range(1, len(points)):
            heappush(candidate_points, [-self.distance(points[idx]), points[idx]])
            # check if we have exceeded our limit k
            if len(candidate_points) > k:
                heappop(candidate_points)

        # since points can be returned in any order, no need to use heappop
        # when getting the points from the candidate points
        closest_points = [point[1] for point in candidate_points]

        return closest_points


# Time complexity: O(nlogk) - we iterate through the points and add them to the heap, which takes O(logk) time
# Space complexity: O(k) - we store k points in the heap

if __name__ == "__main__":
    points = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = Solution().kClosest(points, k)
    print(res)
