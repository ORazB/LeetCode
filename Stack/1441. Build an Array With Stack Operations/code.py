from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        # Clean Solution
        
        res = []
        index = 0
        
        # Iterate through numbers from 1 to n
        for num in range(1, n + 1):
            
            # If we have built the target array, we can return
            if index == len(target):
                break
            
            # We always want to push at every iteration
            res.append("Push")
            
            # Check if the current number matches the target at the current index
            if num == target[index]:
                # If it matches, move to the next index in target
                index += 1
            else:
                # If it doesn't match, we push "pop" as in the popped the next num + 1
                res.append("Pop")
        return res