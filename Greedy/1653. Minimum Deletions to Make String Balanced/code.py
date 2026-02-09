class Solution:
    def minimumDeletions(self, s: str) -> int:

        # greedy (2nd solution [cleaner])
        deletions = 0
        count = 0

        for char in s:
            # Count tracks how many b's we've seen so far
            if char == "b":
                count += 1
            else:
                # Decide which one is cheaper to delete "a" or "b"
                deletions = min(deletions + 1, count)
        return deletions