class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = {}
        left, right = 0, 0
        
        currentMax = 0
        
        while right < len(s):
          freq[s[right]] = freq.get(s[right], 0) + 1
          currentMax = max(currentMax, freq[s[right]])
          
          while (right - left + 1) - currentMax > k:
            freq[s[left]] -= 1
            left += 1
          
          res = max(res, right - left + 1)
          right += 1
          
        return res