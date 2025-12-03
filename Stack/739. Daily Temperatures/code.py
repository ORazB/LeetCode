from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n) because of the output array and the stack in the worst case
# O(2n) simplifies to O(n)

# Questions:
# Why can't we sort? Because we need to maintain the original order of days to calculate the number of days until a warmer temperature.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Monotonic Stack Approach (Increasing Stack)
        # Stores indices of the unresolved days array
        stack = []
        # Output array initialized with 0s because if no warmer day is found, the value remains 0
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
          # While stack is not empty and current temperature is greater than the temperature at index stored at the top of the stack
          # This means we have found a warmer day for the day at index stack[-1]
          # Pop the index from the stack and calculate the difference in days
            while stack and temperatures[i] > temperatures[stack[-1]]:
                dayIndex = stack.pop()
                res[dayIndex] = i - dayIndex # Example: If dayIndex is 1 and i is 4, then res[1] = 4 - 1 = 3 days until a warmer temperature
            stack.append(i) # Push current index onto the stack to find its warmer day in future iterations
        return res