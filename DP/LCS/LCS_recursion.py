# 1143. Longest Common Subsequence --
"""
Given two strings text1 and text2, 
return the length of their longest common subsequence. 
If there is no common subsequence, return 0.
"""
class Solution:
    def func(self, i, j, text1, text2, n1, n2):
        # ------------------------------------------------------------
        # Base Case:
        # If either string is exhausted (i or j < 0), 
        # no common subsequence is possible.
        # Return 0 in that case.
        # ------------------------------------------------------------
        if i < 0 or j < 0:
            return 0

        # ------------------------------------------------------------
        # If characters match at the current index in both strings,
        # we include it in the LCS and move both indices backward.
        # ------------------------------------------------------------
        if text1[i] == text2[j]:
            return 1 + self.func(i - 1, j - 1, text1, text2, n1, n2)

        # ------------------------------------------------------------
        # If characters don't match, we try both possibilities:
        # 1. Skip current character from text1 (i-1)
        # 2. Skip current character from text2 (j-1)
        # Take the maximum of both.
        # ------------------------------------------------------------
        return max(
            self.func(i - 1, j, text1, text2, n1, n2),   # exclude from text1
            self.func(i, j - 1, text1, text2, n1, n2)    # exclude from text2
        )

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # ------------------------------------------------------------
        # Entry point:
        # We compare from the last characters of both strings
        # (since we're going in reverse).
        # ------------------------------------------------------------
        n1, n2 = len(text1), len(text2)
        return self.func(n1 - 1, n2 - 1, text1, text2, n1, n2)

# ------------------------------------------------------------
# 🧠 Intuition:
# The Longest Common Subsequence (LCS) problem asks for the
# longest sequence that appears **in the same relative order**
# in both strings (but not necessarily contiguously).
#
# We use recursion to explore all possibilities of matching
# and skipping characters from both strings.
#
# Example:
# text1 = "abcde", text2 = "ace"
# LCS = "ace" → length = 3
#
# If characters match: include it and move both pointers.
# If they don't: skip one from either string and take max.
# ------------------------------------------------------------

# ------------------------------------------------------------
# ⏱ Time Complexity: O(2^(n1 + n2))
# Reason: At each step, we branch into 2 calls — so exponential.
# 
# 🧠 Space Complexity: O(n1 + n2)
# Reason: Maximum depth of recursion stack.
# 
# 🔥 Note: This can be optimized using memoization or tabulation.
# ------------------------------------------------------------
