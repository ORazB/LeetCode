from typing import List

# Time Complexity: O(nlogn) due to sorting
# Space Complexity: O(1)

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
      
        # Calculate total apples left to redistribute
        appleLeft = sum(apple)
        # Sort capacities in ascending order
        capacity.sort()
        
        # Start from the largest capacity box
        index = len(capacity) - 1
        res = 0
        
        # Distribute apples into boxes until all apples are redistributed
        while appleLeft > 0:
            appleLeft -= capacity[index]
            index -= 1
            res += 1
        return res
        