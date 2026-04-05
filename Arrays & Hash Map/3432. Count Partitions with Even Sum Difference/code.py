from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1)

# Why This Works:

# The sum difference of two partitions is even if the total sum of the array is even.
# If the total sum is odd, it's impossible to split it into two partitions with an even

# Why we return n - 1?
# Because of this 0 <= i < n - 1
# If the sum is even, we can choose any index from 0 to n-2 to split the array into two non-empty partitions.

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0