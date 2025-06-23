class Solution:
    def findLCS(self, n1: int, n2: int, text1: str, text2: str) -> str:
        # Intuition:
        # We're finding the Longest Common Subsequence (LCS) between two strings.
        # LCS is the longest sequence that appears in the same relative order in both strings, but not necessarily contiguously.

        # dp[i][j] represents the length of LCS between text1[0...i-1] and text2[0...j-1]
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]  # +1 for index shifting to handle base case (empty strings)

        # Step 1: Build the dp table
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match → include it in LCS
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Characters do not match → take the max by ignoring one char from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 2: Reconstruct the LCS from the dp table
        lcs = dp[n1][n2]  # Length of LCS
        res = []
        i, j = n1, n2

        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                # If current characters in both strings are equal, include in LCS
                res.append(text1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                # Move up in dp table
                i -= 1
            else:
                # Move left in dp table
                j -= 1

        # Since we added LCS characters in reverse order, reverse the result
        return ''.join(res[::-1])

# --------------------------------------------------
# 🔍 Example: text1 = "abcde", text2 = "ace"
# LCS is "ace"
#
# Final dp table:
#     a c e
#   0 0 0 0
# a 1 1 1
# b 1 1 1
# c 1 2 2
# d 1 2 2
# e 1 2 3
#
# From dp[5][3] = 3, backtrack gives "ace"
# --------------------------------------------------

# ✅ Time Complexity: O(n1 * n2)
# ✅ Space Complexity: O(n1 * n2)
