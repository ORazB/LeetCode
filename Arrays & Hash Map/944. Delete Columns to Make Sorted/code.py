from typing import List

# Time Complexity: O(N * M)
# N = number of strings (rows)
# M = length of each string (columns)
# Space Complexity: O(1)

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        # Count of columns that must be deleted
        res = 0

        # Iterate over each column
        for col in range(len(strs[0])):
            
            # Initialize with the first row's character in this column
            prev = strs[0][col]
            
            # Compare characters down the column
            for row in range(1, len(strs)):
                if strs[row][col] >= prev:
                    # Update previous character for lexicographic comparison
                    prev = strs[row][col]
                else:
                    # Column is not sorted; mark it for deletion
                    res += 1
                    break

        return res