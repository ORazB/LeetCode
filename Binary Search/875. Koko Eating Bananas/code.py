from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Binary Search (Eating Speed)

        low, high = 1, max(piles)
        ans = max(piles)

        while low <= high:
            mid = (low + high) // 2

            totalHour = 0
            for pile in piles:
                totalHour += math.ceil(pile / mid) # Mid is the eating speed
            
            if totalHour <= h:
                # Update answer everytime totalHour is below h because we want to find the minimum
                high = mid - 1
                ans = min(ans, mid)
            else:
                low = mid + 1
        return ans