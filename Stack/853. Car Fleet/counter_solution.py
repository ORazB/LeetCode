from typing import List

# Time Complexity: O(N log N) because of sorting
# Space Complexity: O(N) for the pair list

# Questions:
# Why do we need to sort it in reverse order?
# Because we want to process the cars starting from the one closest to the target to the farthest.

# Why do we update currentTime only when we find a slower car?
# Because a car that takes longer to reach the target cannot catch up to a car that is already ahead of it.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Counter Solution
        
        pair = [[p, s] for p, s in zip(position, speed)]

        counter = 0
        currentTime = 0 # Stores the slowest car

        # Sort the pair based on position in descending order because we want to process cars from closest to target to farthest
        for p, s in sorted(pair)[::-1]:
            distanceTime = ((target - p) / s)

            # If the current car takes more time than the slowest car, it forms a new fleet
            if currentTime < distanceTime:
                counter += 1
                currentTime = distanceTime # Update the slowest car time
        return counter