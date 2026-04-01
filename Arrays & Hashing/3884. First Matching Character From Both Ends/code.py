class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        
        # First Solution
        if len(s) <= 1:
            return 0
        
        for i in range(len(s)):
            if s[i] == s[len(s) - i - 1]:
                return min(i, len(s) - i - 1)
        return -1