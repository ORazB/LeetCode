from typing import List

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Brute Force Approach

# Very intuitive approach where we try to form two partitions such that their sum difference is even.
# sum() is called multiple times leading to O(n^2) time complexity.

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        left = [nums[0]]
        right = nums[1:]

        count = 0

        for i in range(1, len(nums)):
            if (sum(left) - sum(right)) % 2 == 0:
                right.remove(nums[i])
                left.append(nums[i])
                count += 1
        return count