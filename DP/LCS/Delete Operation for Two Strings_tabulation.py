class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # n1 + n2 - (2 * lcs)
        n1, n2 = len(word1), len(word2)
        # def func(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if word1[i] == word2[j]:
        #         dp[i][j] = 1 + func(i - 1, j - 1)
        #         return dp[i][j]
        #     dp[i][j] = max(func(i - 1, j), func(i, j - 1))
        #     return dp[i][j]
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        lcs = dp[n1][n2]
        return n1 + n2 - (2 * lcs)