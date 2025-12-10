from typing import List

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # Edge cases
        if len(nums) == 1: return nums[0]
        if nums[0] < nums[len(nums) - 1]: return nums[0]

        while left < right:
            mid = (left + right) // 2
            
            # Check if mid is the pivot point
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # Check if mid-1 is the pivot point
            elif nums[mid] < nums[mid - 1]:
                return nums[mid] 
              
            # Decide which side to search next
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return -1