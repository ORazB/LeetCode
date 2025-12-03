from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        maxLeft = height[left]
        maxRight = height[right]
        
        result = 0

        while left < right:

            water = 0
            
            # Move the pointer with the smaller max height
            if maxLeft < maxRight:
                left += 1

                maxLeft = max(maxLeft, height[left])
                water = maxLeft - height[left]
            # Move right pointer if maxRight is smaller
            else:
                right -= 1

                maxRight = max(maxRight, height[right])
                water = maxRight - height[right]
            result += water
        return result