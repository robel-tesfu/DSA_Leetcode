from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        numbers = [str(i) for i in range(1, n + 1)]

        k -= 1          # convert to 0-based index

        answer = []

        for i in range(n, 0, -1):

            block = factorial(i - 1)

            index = k // block

            answer.append(numbers.pop(index))

            k %= block

        return "".join(answer)