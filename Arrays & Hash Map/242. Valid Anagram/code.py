from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1) - Since the character set is fixed (assuming only lowercase letters)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Frequency dictionary to count occurrences of each character
        counterS = {}
        counterT = {}

        # Count frequency of each character in both strings
        for char in s:
            counterS[char] = counterS.get(char, 0) + 1

        for char in t:
            counterT[char] = counterT.get(char, 0) + 1
        
        # Compare frequency dictionaries
        return counterS == counterT
        