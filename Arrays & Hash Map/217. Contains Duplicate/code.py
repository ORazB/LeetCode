from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # HashSet to store seen numbers
        seen = set()

        for num in nums:
            
            # If number is already in the set, we found a duplicate
            if num in seen:
                return True
            # Add number to the set
            seen.add(num)

        return False