# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Hash map to hold the mappings of closing to opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If it's an opening bracket, push onto stack
            if char in mapping.values():
                stack.append(char)
            # If it's a closing bracket, check for matching opening bracket
            elif char in mapping.keys():
                # If stack is empty or top of stack doesn't match, return False
                if not stack or mapping[char] != stack.pop():
                    return False
        # If stack is empty, all brackets were matched
        return not stack