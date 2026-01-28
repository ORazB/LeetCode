# Time Complexity: O(N) where N is the length of s2
# Space Complexity: O(1) since the size of the count dictionaries is bounded by the number of unique characters (26 for lowercase English letters)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      
        # Check if s1 is longer than s2 because in that case it's impossible for s2 to contain a permutation of s1
        if len(s1) > len(s2):
            return False

        s1Count = {}
        s2Count = {}
        
        # Initialize the character count for s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            s2Count[s2[i]] = s2Count.get(s2[i], 0) + 1
        
        # Check the first window
        if s1Count == s2Count:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            # Add the new character to the window
            s2Count[s2[right]] = s2Count.get(s2[right], 0) + 1
            
            # Remove the leftmost character from the window
            s2Count[s2[left]] -= 1

            # Clean up the count dictionary
            # If we don't remove the zero count, the comparison will fail
            if s2Count[s2[left]] == 0:
                del s2Count[s2[left]]
            
            left += 1

            if s1Count == s2Count:
                return True
        return False