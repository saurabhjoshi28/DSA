class Solution:
    def minInsertions(self, s: str) -> int:
        s1, s2 = s, s[::-1]
        n1, n2 = len(s1), len(s2)
        # def func(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if s1[i] == s2[j]:
        #         dp[i][j] = 1 + func(i - 1, j - 1)
        #         return dp[i][j]
        #     dp[i][j] = max(func(i, j - 1), func(i - 1, j))
        #     return dp[i][j]
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            dp[i][0] = 0
        for j in range(n2 + 1):
            dp[0][j] = 0
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lps = dp[n1][n2]
        return n1 - lps