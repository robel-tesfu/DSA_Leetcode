class Solution:
    def isNumber(self, s: str) -> bool:
        seenDigit = False
        seenDot = False
        seenExponent = False

        for i, ch in enumerate(s):

            if ch.isdigit():
                seenDigit = True

            elif ch in "+-":
                if i != 0 and s[i - 1] not in "eE":
                    return False

            elif ch == ".":
                if seenDot or seenExponent:
                    return False
                seenDot = True

            elif ch in "eE":
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                seenDigit = False   # must have digits after exponent

            else:
                return False

        return seenDigit