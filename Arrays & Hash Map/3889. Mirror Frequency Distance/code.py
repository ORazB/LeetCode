class Solution:
    def mirrorFrequency(self, s: str) -> int:

        freqC = {}
        res = 0
        
        # Build frequencies
        for char in s:
            freqC[char] = freqC.get(char, 0) + 1
            
        # For marking already visited pair
        marked = {}
        
        # Loop only unique char
        for char in freqC.keys():
            # Handle mirror for number & character
            if char.isnumeric():
                mirror = chr(ord('0') + ord('9') - ord(char))
            else:
                mirror = chr(ord('a') + ord('z') - ord(char))
            
            # If marked skip
            if char in marked or mirror in marked:
                continue
            
            # If mirror is not in freqC then substract by 0
            if mirror not in freqC:
                res += abs(freqC[char] - 0)
            else:
                res += abs(freqC[char] - freqC[mirror])
            
            # Mark the pair
            marked[char] = mirror
            marked[mirror] = char
        return res