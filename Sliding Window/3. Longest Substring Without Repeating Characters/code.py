# Time Complexity: O(n)
# Space Complexity: O(min(n, m)) where m is the size of the character set and n is the length of the string
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
        # Why set as our data structure?
        # Because we need to check if a character is already in the substring, and a set provides constant time lookup.
        seen = set()
        res = 0
        
        left = 0
        right = 0
        
        # Why 2 pointers are the same?

        # Because we are using a sliding window approach, the left pointer represents the start of the current substring,
        # and the right pointer represents the end of the current substring. As we iterate through the string, we move the right pointer
        # to the right and add the character at the right pointer to the set. If the character is already in the set, we move the left pointer
        # to the right until the character is no longer in the set. This way, we always have a substring without repeating characters.
      
        while right < len(s):
          
            # Always remove the leftmost character from the set if it is in the set
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            
            # Why left + 1?
            # Because we want to include the character at the right pointer in the length of the substring.
            # If we don't add 1, we would be excluding the character at the right pointer from the length of the substring.
            res = max(res, right - left + 1)
            right += 1
        return res
