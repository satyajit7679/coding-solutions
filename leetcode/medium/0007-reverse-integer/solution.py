class Solution:
    def reverse(self, x: int) -> int:

        # Remember whether x is positive or negative
        sign = -1 if x < 0 else 1

        # Work with positive number
        x = abs(x)

        rev = 0

        while x > 0:

            # Get last digit
            digit = x % 10

            # Remove last digit
            x = x // 10

            # Check if adding this digit causes overflow
            if rev > (2**31 - 1 - digit) // 10:
                return 0

            # Add digit to reversed number
            rev = rev * 10 + digit

        # Put the original sign back
        return sign * rev