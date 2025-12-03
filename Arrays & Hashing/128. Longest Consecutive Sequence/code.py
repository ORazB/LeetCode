from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        # Create a set of numbers for O(1) lookups
        numSet = set(nums)
        maxLength = 0
        
        # Iterate through each number in the set
        for num in numSet:
          
            # Check if it's the start of a sequence
            if num - 1 not in numSet:
                current = num
                currentLength = 1
                
                # Count the length of the sequence
                while current + 1 in numSet:
                    current += 1
                    currentLength += 1
                # Update the maximum length found
                maxLength = max(currentLength, maxLength)
        return maxLength