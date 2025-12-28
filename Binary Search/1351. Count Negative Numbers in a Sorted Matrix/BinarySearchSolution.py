from typing import List

# Time Complexity: O(m log n)
# Space Complexity: O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        # Binary Search
        result = 0

        for array in grid:
            left = 0
            right = len(array) - 1

            firstNegativeIndex = len(array)

            while left <= right:
                mid = (left + right) // 2
                if array[mid] < 0:
                    firstNegativeIndex = mid
                    right = mid - 1
                elif array[mid] >= 0:
                    left = mid + 1
            result += len(array) - firstNegativeIndex
        return result