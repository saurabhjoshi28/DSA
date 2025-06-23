class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1, s2 = s, s[::-1]
        n1, n2 = len(s1), len(s2)
        def func(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s1[i] == s2[j]:
                dp[i][j] = 1 + func(i - 1, j - 1)
                return dp[i][j]
            dp[i][j] = max(func(i, j - 1), func(i - 1, j))
            return dp[i][j]
        dp = [[-1] * n2 for _ in range(n1)]
        return func(n1 - 1, n2 - 1)