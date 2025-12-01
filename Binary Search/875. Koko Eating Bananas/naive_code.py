from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Binary Search (Eating Speed)

      ans = max(piles)
      eatingSpeed = 1

      while eatingSpeed <= max(piles):

            totalHour = 0
            # Calculate the total hour
            for pile in piles:
                totalHour += math.ceil(pile / eatingSpeed)

            if totalHour <= h:
                ans = min(ans, eatingSpeed)
            eatingSpeed += 1
      return ans