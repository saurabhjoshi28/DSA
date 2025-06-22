class Solution:
    def func(self, i, j, text1, text2, n1, n2, dp):
        # ------------------------------------------------------------
        # Base Case:
        # If either string is exhausted (index < 0), return 0.
        # No characters left to match = no LCS.
        # ------------------------------------------------------------
        if i < 0 or j < 0:
            return 0

        # ------------------------------------------------------------
        # If this subproblem has already been solved, return the result.
        # Avoids recomputation (top-down memoization).
        # ------------------------------------------------------------
        if dp[i][j] != -1:
            return dp[i][j]

        # ------------------------------------------------------------
        # Case 1: Characters match → part of LCS.
        # Move diagonally (i-1, j-1) and add 1.
        # ------------------------------------------------------------
        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.func(i - 1, j - 1, text1, text2, n1, n2, dp)
            return dp[i][j]

        # ------------------------------------------------------------
        # Case 2: Characters do not match → explore both options:
        # a) Skip from text1 → move to (i-1, j)
        # b) Skip from text2 → move to (i, j-1)
        # Take the max of both.
        # ------------------------------------------------------------
        dp[i][j] = max(
            self.func(i - 1, j, text1, text2, n1, n2, dp),
            self.func(i, j - 1, text1, text2, n1, n2, dp)
        )
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # ------------------------------------------------------------
        # Entry point:
        # Initialize the dp table with -1 (uncomputed state).
        # ------------------------------------------------------------
        n1, n2 = len(text1), len(text2)
        dp = [[-1] * n2 for _ in range(n1)]
        return self.func(n1 - 1, n2 - 1, text1, text2, n1, n2, dp)

# ------------------------------------------------------------
# 🧠 Intuition:
# We're trying to find the longest subsequence that appears in
# both strings in the same order.
# 
# Use recursion to try both possibilities at every step:
# - If characters match → take it and move both pointers.
# - If not → skip one character from either string.
#
# Memoization saves overlapping subproblem results in a 2D table.
# ------------------------------------------------------------

# ------------------------------------------------------------
# ⏱ Time Complexity: O(n1 * n2)
# Each (i, j) state is computed only once and stored in dp.
#
# 🧠 Space Complexity: O(n1 * n2) + O(n1 + n2) recursion stack
# (dp table + recursive call stack)
# ------------------------------------------------------------
