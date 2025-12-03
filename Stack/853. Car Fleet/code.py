from typing import List

# Time Complexity: O(N log N) because of sorting
# Space Complexity: O(N) for the pair list

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Stack Solution

        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # Sort the pair based on position in descending order because we want to process cars from closest to target to farthest
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s) # Calculate the distance time and append it

            if len(stack) >= 2 and stack[-1] <= stack[-2]: # If it collides then it will get blocked so it will be a single fleet
                stack.pop() # Remove the top of the stack to combine the fleet
        return len(stack)