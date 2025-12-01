from typing import List
import math

# Naive Approach

# Time Complexity: O(n * m) where n is number of piles and m is the max pile size
# Space Complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

    # Initialize the answer with the maximum pile size
      ans = max(piles)
      eatingSpeed = 1
      
      
    # Iterate through all possible eating speeds from 1 to max pile size
      while eatingSpeed <= max(piles):

            totalHour = 0
            # Calculate total hours needed at the current eating speed
            for pile in piles:
                totalHour += math.ceil(pile / eatingSpeed)
            # If total hours is within the limit, update the answer
            if totalHour <= h:
                ans = min(ans, eatingSpeed)
            eatingSpeed += 1
      return ans