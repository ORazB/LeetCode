import string


class Solution:
    def reverseByType(self, s: str) -> str:

        letters = {
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        }

        if len(s) == 1:
            return s[0]
        if len(s) == 0:
            return "-1"

        left, right = 0, len(s) - 1
        stringInput = list(s)

        while left < right:
            print(stringInput[left], stringInput[right])
            if stringInput[left] in letters and stringInput[right] in letters:
              temp = stringInput[left]
              stringInput[left] = stringInput[right]
              stringInput[right] = temp
              
              left += 1
              right -= 1
            elif not stringInput[left] in letters:
                left += 1
            elif not stringInput[right] in letters:
                right -= 1
        
        left, right = 0, len(s) - 1
        
        while left < right:
            print(stringInput[left], stringInput[right])
            if stringInput[left] not in letters and stringInput[right] not in letters:
              temp = stringInput[left]
              stringInput[left] = stringInput[right]
              stringInput[right] = temp
              
              left += 1
              right -= 1
            elif stringInput[left] in letters:
                left += 1
            elif stringInput[right] in letters:
                right -= 1
        return "".join(stringInput)