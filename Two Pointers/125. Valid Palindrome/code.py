# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
      
        # Preprocess the string to remove non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        left, right = 0, len(s) - 1
        for i in range(len(s)):
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True