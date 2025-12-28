from typing import List

# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        row = 0
        col = len(grid[0]) - 1

        while row < len(grid) and col >= 0:
            if grid[row][col] < 0:
                result += len(grid) - row
                col -= 1
            else:
                row += 1
        return result