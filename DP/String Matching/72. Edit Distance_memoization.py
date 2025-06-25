class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        def func(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = func(i - 1, j - 1)
                return dp[i][j]
            insert = 1 + func(i, j - 1)
            delete = 1 + func(i - 1, j)
            replace = 1 + func(i - 1, j - 1)
            dp[i][j] = min(insert, delete, replace)
            return dp[i][j]
        dp = [[-1] * n2 for _ in range(n1)]
        return func(n1 - 1, n2 - 1)