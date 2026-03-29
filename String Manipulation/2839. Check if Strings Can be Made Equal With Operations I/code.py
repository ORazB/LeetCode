class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        # O(n) solution (hash set)
        if len(s1) != len(s2):
            return False
        
        s1Even = {}
        s1Odd = {}
        s2Even = {}
        s2Odd = {}
        
        for i in range(len(s1)):
            if i % 2 == 0:
                s1Even[s1[i]] = s1Even.get(s1[i], 0) + 1
                s2Even[s2[i]] = s2Even.get(s2[i], 0) + 1
            else:
                s1Odd[s1[i]] = s1Odd.get(s1[i], 0) + 1
                s2Odd[s2[i]] = s2Odd.get(s2[i], 0) + 1
        
        return s1Even == s2Even and s1Odd == s2Odd