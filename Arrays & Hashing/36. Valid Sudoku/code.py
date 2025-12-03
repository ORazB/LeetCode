from typing import List

# Hashing Approach

# Time Complexity: O(1) since the board size is fixed (9x9)
# Space Complexity: O(1) since we use fixed size data structures

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      
      # Initialize data structures to track seen numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

      # Iterate through each cell in the board
        for r in range(9):
          # Iterate through each column in the row
            for c in range(9):
                
                # Get the current number
                num = board[r][c]
                
                # Skip empty cells
                if num == ".":
                    continue
                  
                # Calculate the index of the 3x3 sub-box
                # Example: for cell (4,5), the 3x3 box index is (4//3)*3 + (5//3) = 1*3 + 1 = 4
                # Mutliply by 3 because there are 3 boxes in each row of boxes
                boxIndex = (r // 3) * 3 + (c / 3)
                
                # Return false if the number is already seen in the current row, column, or box
                if num in rows[r] or num in cols[c] or num in boxes[boxIndex]:
                    return False
                  
                # Mark the number as seen in the current row, column, and box
                rows[r].add(num)
                cols[c].add(num)
                boxes[boxIndex].add(num)
        return True