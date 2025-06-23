class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1, s2 = s, s[::-1]
        n1, n2 = len(s1), len(s2)
        # dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        curr, prev = [0] * (n2 + 1), [0] * (n2 + 1)
        # base case
        # for i in range(n1 + 1):
        #     dp[i][0] = 0
        # for j in range(n2 + 1):
        #     dp[0][j] = 0
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr[:]
        return prev[n2]