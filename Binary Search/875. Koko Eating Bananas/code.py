from typing import List
import math

# Time Complexity: O(N log M) where N is the number of piles and M is the maximum number of bananas in a pile.
# Space Complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Binary Search on the eating speed
        
        # Define the search space for eating speed
        low, high = 1, max(piles)
        
        # Initialize answer with the maximum possible eating speed
        ans = max(piles)

        while low <= high:
            # Find the mid eating speed
            mid = (low + high) // 2

            # Calculate total hours needed to eat all piles at speed mid
            totalHour = 0
            for pile in piles:
                totalHour += math.ceil(pile / mid) # Calculate hours needed for each pile where mid is the eating speed
            
            # Adjust search space based on total hours needed
            if totalHour <= h:
                # If Koko can finish eating at speed mid within h hours, try a slower speed
                high = mid - 1
                ans = min(ans, mid)
            else:
                # If Koko cannot finish eating at speed mid within h hours, try a faster speed
                low = mid + 1
        return ans