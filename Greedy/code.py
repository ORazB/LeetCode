from typing import List

# Time Complexity: O(N log N)
# Space Complexity: O(1)

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        happiness = sorted(happiness, reverse=True)
        childCount = 0
        chosenChild = 0

        for i in range(k):
            child = happiness[i] - childCount
            if child < 0:
                # No point in choosing further children as their happiness will be negative
                break
            chosenChild += child
            childCount += 1
        return chosenChild
        