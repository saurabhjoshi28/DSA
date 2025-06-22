class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)

        # ------------------------------------------------------------
        # Create a 2D DP table initialized with 0s.
        # dp[i][j] represents LCS length of text1[0...i-1] and text2[0...j-1]
        # Extra row and column added for index shifting (1-based)
        # ------------------------------------------------------------
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # ------------------------------------------------------------
        # Fill the DP table using bottom-up approach
        # ------------------------------------------------------------
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match → include in LCS
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Characters don't match → take max of left and top
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # ------------------------------------------------------------
        # Final result is in dp[n1][n2] → full lengths of both strings
        # ------------------------------------------------------------
        return dp[n1][n2]

# ------------------------------------------------------------
# 🧠 Intuition:
# We use bottom-up DP to build the LCS lengths for all prefixes
# of text1 and text2.
# At each cell dp[i][j], we determine the LCS of text1[0..i-1]
# and text2[0..j-1] using previously computed results.
#
# The recurrence:
# If characters match:    dp[i][j] = 1 + dp[i-1][j-1]
# If not match:           dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# ------------------------------------------------------------

# ------------------------------------------------------------
# ⏱ Time Complexity: O(n1 * n2)
# Fill each of the n1 x n2 entries once.

# 💾 Space Complexity: O(n1 * n2)
# Used for the DP table.
#
# Note: This can be optimized to O(n2) using 2 rows instead.
# ------------------------------------------------------------
