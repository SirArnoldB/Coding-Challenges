"""
# Number of Islands
-------------------
Source: https://leetcode.com/problems/number-of-islands/
- Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
- An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
- You may assume all four edges of the grid are all surrounded by water.

# Example 1:

    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]

    # Output: 1

# Example 2:

    # Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]

    # Output: 3

# Constraints:
    # m == grid.length
    # n == grid[i].length
    # 1 <= m, n <= 300
    # grid[i][j] is '0' or '1'.
"""


class Solution:
    def cellNotValid(self, grid, row, col, rows, cols):
        return row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != "1"

    def dfs(self, grid, row, col, rows, cols):
        if self.cellNotValid(grid, row, col, rows, cols):
            return

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        grid[row][col] = "#"

        for dir in directions:
            self.dfs(grid, row + dir[0], col + dir[1], rows, cols)

    def numIslands(self, grid: list[list[str]]) -> int:
        num_islands = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    # find all the connecting ones
                    self.dfs(grid, row, col, rows, cols)
                    # increment the island count
                    num_islands += 1

        return num_islands
