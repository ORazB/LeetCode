from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:

    # Encode and Decode Strings
    def encode(self, strs: List[str]) -> str:
        result = ""
        
        # Handle edge case for empty input list
        if len(strs) <= 0:
            return result

        # Encode each string with its length and a delimiter
        # Delimiter used is '#' and length is prepended before each string
        # So that during decoding we know how many characters to read
        for string in strs:
            result += str(len(string)) + "#" + string
        return result


    def decode(self, s: str) -> List[str]:

        # Decode the encoded string back to list of strings
        result = []
        resultHolder = ""

        i = 0
        # Iterate through the encoded string
        while i < len(s):
            j = i
            
            # Find the delimiter '#' to extract the length of the next string
            while s[j] != "#":
                j += 1
            
            # Extract the length and the actual string using the length
            length = int(s[i:j]) # Example: "4#test" -> length = 4
            word = s[j + 1 : (1 + j + length)] # Exampl: "4#test" -> word = "test"

            # Append the decoded string to the result list
            result.append(word)
            
            # Move the index to the start of the next encoded string
            i = j + 1 + length
        return result