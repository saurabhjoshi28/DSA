class Solution:
    def longestCommonSubstr(self, text1, text2):
        # Intuition:
        # This is similar to the Longest Common Subsequence (LCS), 
        # but with one key difference:
        # ➤ We're looking for the **longest continuous matching substring**,
        #    not just a common sequence. So the characters must match AND be contiguous.

        # Example:
        # text1 = "abcdf", text2 = "abedf"
        # Common substring = "df" → length = 2

        n1, n2 = len(text1), len(text2)
        # dp[i][j] will store the length of longest common substring 
        # ending at index (i-1) in text1 and (j-1) in text2
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        ans = 0  # to keep track of the maximum length found

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    # If characters match, extend the previous substring
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])
                else:
                    # ❗ Key difference from LCS:
                    # If characters do not match, we break continuity,
                    # so we reset dp[i][j] to 0 (no common substring ends here)
                    dp[i][j] = 0

        return ans

# --------------------------------------------------
# 🔍 Example: text1 = "abcde", text2 = "abfce"
#
# Common substrings:
# - "ab" → length 2
# - "c" → length 1
# Final answer = 2
#
# dp table when comparing "abcde" vs "abfce":
#   a b f c e
# a 1 0 0 0 0
# b 0 2 0 0 0
# c 0 0 0 1 0
# d 0 0 0 0 0
# e 0 0 0 0 1
# --------------------------------------------------

# ✅ Time Complexity: O(n1 * n2)
# ✅ Space Complexity: O(n1 * n2)
