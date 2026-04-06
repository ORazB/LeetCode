class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Tortoise & Hare Solution
        slow, fast = 0, 0

        # Detect Cycle
        # We left the slow pointer at the intersection point
        for num in nums:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Detect Duplicate
        # When we move a pointer from the start and a pointer from the meeting point at the same speed
        # They will intersect exactly at the cycle entrance (the duplicate number)
        slow2 = 0
        for num in nums:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow2
        return slow2