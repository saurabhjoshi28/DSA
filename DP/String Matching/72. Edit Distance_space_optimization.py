class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        # def func(i, j):
        #     if i < 0:
        #         return j + 1
        #     if j < 0:
        #         return i + 1
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if word1[i] == word2[j]:
        #         dp[i][j] = func(i - 1, j - 1)
        #         return dp[i][j]
        #     insert = 1 + func(i, j - 1)
        #     delete = 1 + func(i - 1, j)
        #     replace = 1 + func(i - 1, j - 1)
        #     dp[i][j] = min(insert, delete, replace)
        #     return dp[i][j]
        # dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        curr, prev = [0] * (n2 + 1), [0] * (n2 + 1)
        # Base cases
        for j in range(n2 + 1):
            prev[j] = j # Because we did index shifting we need to strings are 1-indexed now
        # # for i in range(n1 + 1):
        #     curr[0] = i 
        for i in range(1, n1 + 1):
            curr[0] = i 
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    insert = 1 + curr[j - 1]
                    delete = 1 + prev[j]
                    replace = 1 + prev[j - 1]
                    curr[j] = min(insert, delete, replace)
            prev = curr[:]
        return prev[n2]