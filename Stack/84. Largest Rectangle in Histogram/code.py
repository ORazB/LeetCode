from typing import List

# Time Complexity: O(N) because each bar is pushed and popped at most once
# Space Complexity: O(N) for the stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # Stack (Monotonic Increasing Stack) Solution
        
        largest = 0
        stack = []
        n = len(heights)

        for i, h in enumerate(heights):
            # Condition: Pop until the current height is greater than the height at the top of the stack
            while stack and heights[stack[-1]] > h:
              # Pop the top of the stack and calculate the area
                height = heights[stack.pop()]
                # Calculate the width by checking if the stack is empty
                width = i if not stack else i - stack[-1] - 1

                largest = max(largest, width * height)
            # Push the current index onto the stack
            stack.append(i)

        # Clear the stack for the remaining heights because they can extend to the end
        while stack:
            height = heights[stack.pop()]
            width = n - stack[-1] - 1
            largest = max(largest, width * height)
        
        return largest