from typing import List

# Time Complexity: O(N^2)
# Space Complexity: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        # Sort the array to use two pointers approach
        nums.sort()
        
        for i in range(len(nums)):
            # Skip duplicate values for the first number    
            if i > 0 and nums[i] == nums[i - 1]:
                continue
              
            k = len(nums) - 1
            j = i + 1
            
            # Why j and not i? Because we are looking for triplets, so the second pointer should start just after the first pointer
            # Why is it not possible for the answer will be (j) below i? Because the array is sorted and we are looking for triplets that sum to zero.
            # Are we shrinking every iteration? Yes, because we are moving either j or k closer to each other.
            while j < k:
                numSum = nums[i] + nums[j] + nums[k]

                if numSum < 0:
                    j += 1
                elif numSum > 0:
                    k -= 1
                else:
                    # Found a triplet
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # Move both pointers to find the next unique triplet
                    k -= 1
                    j += 1
                    
                    # Skip duplicate values for the third number
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res