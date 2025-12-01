from typing import List

# Time Complexity: O(log n)
# Space Complexity: O(1)

# New Topic: Binary Search

# Time Complexity O(log n) Explanation:
# The algorithm divides the search space in half with each iteration,

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Initialize left and right pointers
        left = 0
        right = len(nums) - 1

        # Calculate mid index
        mid = (left + right) // 2

        while left <= right:
            # Check if mid element is the target
            if nums[mid] == target:
                return mid

            # Adjust search boundaries based on comparison
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
            # Recalculate mid index
            mid = (left + right) // 2
        # Target not found
        return -1