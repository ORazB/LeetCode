
# Note:
# Counter doesn't work because the strict constraint (it's too slow).

# That's why we need to find a formula to calculate the number of odd numbers in the range [low, high].
# The formula is as follows:
# 1. If low is even, increment low by 1 to make it odd.
# 2. If high is even, decrement high by 1 to make it odd.
# 3. The number of odd numbers in the range [low, high] can be calculated using the formula: (high - low) // 2 + 1.

# Why this works?
# I HAVE NO IDEA LOL, I'LL COME BACK TO THIS LATER. 12/7/2025 (Still on Binary Search Topic, Math is the last topic.)

class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if low % 2 == 0:
            low = low + 1
        if high % 2 == 0:
            high = high - 1
        
        return  (high - low) // 2 + 1