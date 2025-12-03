from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Initialize two pointers
        left = 0
        right = len(numbers) - 1

        for _ in range(len(numbers) - 1):
          
          # Calculate the sum of the two pointers
            sumNum = numbers[left] + numbers[right]

          # Check if the sum matches the target
            if sumNum == target:
                return [left + 1, right + 1]
            elif sumNum < target:
                left += 1
            else:
                right -= 1