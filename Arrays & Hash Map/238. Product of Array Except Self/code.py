from typing import List
import math

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        # Initialize prefix and suffix products  
        prefix = 1
        suffix = 1

        # Initialize the result array with 1s
        result = [1] * len(nums)

        # Multiplies the prefix products
        # Example: nums = [1,2,3,4] -> result after prefix pass = [1,1,2,6]
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
        
        # Multiplies the suffix products
        # Example: result = [1,1,2,6] -> result after suffix pass = [24,12,8,6]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result