class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        def func(i, j):
            if j < 0 and i < 0:
                return True
            if j < 0 and i >= 0:
                return False
            if j >= 0 and i < 0:
                """
                so in order to match to empty string
                all remaining has to be '*'
                """
                for c in range(j + 1):
                    if p[c] != '*':
                        return False
                return True
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = func(i - 1, j - 1)
                return dp[i][j]
            elif p[j] == '*':
                matches_empty = func(i, j - 1)
                matches_a_character = func(i - 1, j)
                dp[i][j] = matches_empty or matches_a_character
                return dp[i][j]
            else:
                dp[i][j] = False
                return dp[i][j]
        dp = [[-1] * n2 for _ in range(n1)]
        return func(n1 -1, n2 - 1)