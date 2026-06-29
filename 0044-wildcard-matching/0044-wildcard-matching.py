class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        prev = [False] * (n + 1)
        curr = [False] * (n + 1)

        # Empty string matches empty pattern
        prev[n] = True

        # Initialize last row (empty string vs remaining pattern)
        for j in range(n - 1, -1, -1):
            if p[j] == '*':
                prev[j] = prev[j + 1]
            else:
                break

        for i in range(m - 1, -1, -1):
            curr = [False] * (n + 1)

            for j in range(n - 1, -1, -1):

                if p[j] == '*':
                    curr[j] = curr[j + 1] or prev[j]

                elif p[j] == '?' or s[i] == p[j]:
                    curr[j] = prev[j + 1]

            prev = curr

        return prev[0]