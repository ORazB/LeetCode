from typing import List

# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) as we only use a constant amount of extra space

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        # float("inf") is a special floating-point value that represents positive infinity.
        # It is used here to initialize minDiff to a very large value so that any difference
        # between array elements will be smaller than minDiff.

        minDiff = float("inf")
        result = []
        
        for i in range(len(arr) - 1):
          # Initialize currentDiff to the difference between the next element and the current element.
          # Why next element? Because we are comparing the difference between consecutive elements.
          currentDiff = arr[i + 1] - arr[i]
          
          # If the current difference is smaller than the minimum difference, update minDiff and reset result.
          if currentDiff < minDiff:
            minDiff = currentDiff
            result = [[arr[i], arr[i + 1]]]
          # If the current difference is equal to the minimum difference, append the pair to result.
          elif currentDiff == minDiff:
            result.append([arr[i], arr[i + 1]])
        return result