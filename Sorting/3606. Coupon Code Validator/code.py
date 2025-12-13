from typing import List

# Time Complexity: O(n log n) sorting + O(n) validation = O(n log n)
# Space Complexity: O(n)


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:

        res = []

        # Create tuples of (code, businessLine, isActive) for easier processing
        tupleTest = [
            [c, b, active] for c, b, active in zip(code, businessLine, isActive)
        ]

        priorityOrder = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }

        for code, business, active in tupleTest:

            # Validate code
            if code == "":
                continue

            # Check if all characters are alphanumeric or underscore
            valid = True
            for char in code:
                if not (char.isalnum() or char == "_"):
                    valid = False
                    break

            # Skip invalid codes
            if not valid:
                continue

            # Validate business line
            if (
                business != "electronics"
                and business != "grocery"
                and business != "pharmacy"
                and business != "restaurant"
            ):
                continue

            # Check if active
            if not active:
                continue

            # If all validations pass, add to result
            res.append([code, business])
        # Sort first by business line priority, then lexicographically by code

        # What's lexicographical order?
        # Lexicographical order is similar to dictionary order.
        # It means that strings are compared character by character based on their ASCII values.
        res = sorted(res, key=lambda x: (priorityOrder[x[1]], x[0]))

        # Extract only the codes for the final output
        return [code for code, _ in res]
