from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)

# Bucket Sort Approach

# Bucket sort is used to group elements based on their frequency.
# We create an array of lists (buckets) where the index represents the frequency of elements.
# This allows us to efficiently gather the top k frequent elements.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Frequency dictionary to count occurrences of each number
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        # Create buckets where index represents frequency
        freq = [[] for num in range(len(nums) + 1)]

        # Place numbers in their respective frequency buckets
        for key, value in counter.items():
            freq[value].append(key)
        
        result = []
        # Gather top k frequent elements from the buckets
        for index in range(len(freq) - 1, -1, -1):

            for n in freq[index]:
                result.append(n)
                # Return once we have k elements
                if len(result) == k:
                    return result