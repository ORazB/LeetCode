# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        
        result = 0
        # Dictionary to map Roman numerals to integers
        romanNum = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

        for i in range(len(s)):
            # Check if the current numeral is less than the next numeral
            # If so, subtract its value; otherwise, add its value
            # Why subtract? Because in Roman numerals, placing a smaller numeral before a larger numeral indicates subtraction
            if i + 1 < len(s) and romanNum[s[i]] < romanNum[s[i + 1]]:
                result -= romanNum[s[i]]
            else:
                result += romanNum[s[i]]
        return result