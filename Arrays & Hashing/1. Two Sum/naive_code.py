from typing import List
import math

# Naive Solution

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute Force: Check every pair
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sumNum = nums[i] + nums[j]

                if sumNum == target:
                    return [i, j]
        return []