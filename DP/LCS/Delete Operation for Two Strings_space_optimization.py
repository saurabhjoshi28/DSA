class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # n1 + n2 - (2 * lcs)
        n1, n2 = len(word1), len(word2)
        # dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        curr, prev = [0] * (n2 + 1), [0] * (n2 + 1)
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(curr[j - 1], prev[j])
            prev = curr[:]
        lcs = prev[n2]
        return n1 + n2 - (2 * lcs)