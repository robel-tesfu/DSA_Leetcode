class Solution:
    def plusOne(self, digits):
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            # Carry occurs
            digits[i] = 0

        # All digits were 9
        return [1] + digits