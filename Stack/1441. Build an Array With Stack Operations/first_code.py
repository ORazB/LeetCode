from typing import List

# Time Complexity: O(n) 
# Space Complexity: O(n)

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        # My Initial Solution
        stack = []
        res = []
        
        count = 0
        index = 0
        
        while len(stack) != target:
            
            # Early return if we have built the target array
            if target == stack:
                return res
            
            # Push or Pop based on the condition
            if target[index] == count + 1:
                count += 1
                stack.append(count)
                res.append("Push")

                index += 1
            
            # If not equal then keep pushing and popping until we find the number
            elif target[index] != count + 1:
                while target[index] != count + 1:
                    count += 1
                    stack.append(count)
                    res.append("Push")
                    index += 1

                    stack.pop()
                    res.append("Pop")
                    index -= 1
        return res