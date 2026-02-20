# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Edge Cases
        if len(t) > len(s):
            return ""
        
        if len(s) == 1 and s[0] == t[0]:
            return s[0]
        
        if len(s) == 1 and s[0] != t[0]:
            return ""
            
        # Initialize Counters
        tCount = {}
        window = {}
        
        # Initialize Result (Indicies) and Length
        res, resLen = [-1, -1], float("infinity")
        
        # Count frequencies of characters in t
        for char in t:
          tCount[char] = tCount.get(char, 0) + 1
        
        # Initialize have and need so we can get O(1) check
        # Instead of checking every character in tCount
        have, need = 0, len(tCount)
        
        # Initialize left pointer
        l = 0
        for r in range(len(s)):
          current = s[r]
          # Update window counter
          window[current] = window.get(current, 0) + 1
          
          # Update have counter if current character is in t and window counter matches tCount
          if current in tCount and window[current] == tCount[current]:
            have += 1
          
          # Shrink window if have == need
          while have == need:
            # Update result
            if (r - l + 1) < resLen:
              res = [l, r]
              resLen = (r - l + 1)
            
            # Shrink window
            window[s[l]] -= 1
            
            # Update have counter if current character is in t and window counter is less than tCount
            if s[l] in tCount and window[s[l]] < tCount[s[l]]:
              have -= 1
            # Update left pointer
            l += 1
        
        # Update res
        l, r = res
        # Return substring
        return s[l:r + 1]