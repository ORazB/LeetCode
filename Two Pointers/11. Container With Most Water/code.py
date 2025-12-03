from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        maxArea = 0

        while left < right:
          # Calculate the area formed between the two pointers
            area = min(height[left], height[right]) * (right - left)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
            # Update maxArea if the current area is larger
            maxArea = max(area, maxArea)
        return maxArea