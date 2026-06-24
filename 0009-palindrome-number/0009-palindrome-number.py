class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers are never palindrome
        # also numbers ending with 0 (except 0 itself) are not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # even length OR odd length (middle digit ignored)
        return x == reversed_half or x == reversed_half // 10