from typing import List
import math

# Time Complexity: O(n)
# Space Complexity: O(n) because of the hash set

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(nums):
            # Get the pair by getting the difference
            difference = target - num

            # If it's in the hash set means it's the pair
            if difference in seen:
                return [i, seen[difference]]
            
            seen[num] = i