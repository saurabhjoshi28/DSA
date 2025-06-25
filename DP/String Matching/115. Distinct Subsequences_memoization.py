class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        def func(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                pick = func(i - 1, j - 1)
                notpick = func(i - 1, j)
                dp[i][j] = pick + notpick
                return dp[i][j]
            else:
                dp[i][j] = func(i - 1, j)
                return dp[i][j]
        dp = [[-1] * n2 for _ in range(n1)]
        return func(n1 - 1, n2 - 1)