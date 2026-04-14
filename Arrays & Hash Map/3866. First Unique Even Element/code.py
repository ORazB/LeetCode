class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for num in seen:
            if num % 2 == 0 and seen[num] == 1:
                return num
        return -1