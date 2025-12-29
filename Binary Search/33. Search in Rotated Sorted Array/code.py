from typing import List

# Time Complexity: O(log n)
# Note: Even if there are 2 binary searches, the time complexity remains O(log n) because constants are ignored in Big O notation.
# Space Complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # If true means left is sorted and do search on the left side
            if nums[mid] >= nums[left]:
                # If target is within left and mid
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1 # Move Left
                else:
                    left = mid + 1
            # If false means right is sorted and do search on the right side
            else:
                # If target is within mid and right
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1 # Move Right
                else:
                    right = mid - 1
        return -1

# Questions:
# Is it possible that the program do searches on both sides?
# No, because in each iteration we are eliminating half of the array based on the sorted side