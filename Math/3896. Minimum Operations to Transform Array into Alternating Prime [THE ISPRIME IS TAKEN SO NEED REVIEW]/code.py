# Time Complexity: O(n sqrt(m))
# Space Complexity: O(m log log m + n)


# helper
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = 0

        for i in range(len(nums)):
            num = nums[i]
            if i % 2 == 0:
                while not isPrime(nums[i]):
                    nums[i] += 1
                    res += 1
            else:
                while isPrime(nums[i]):
                    nums[i] += 1
                    res += 1
        return res
