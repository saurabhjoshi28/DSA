class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)

        # ------------------------------------------------------------
        # 🧠 Striver’s Trick for Space Optimization:
        # In normal tabulation, we use dp[i][j], which depends only on:
        #   - dp[i-1][j-1], dp[i-1][j], and dp[i][j-1]
        #
        # So, we only need the previous row (dp[i-1]) at any time,
        # and the current row being computed (dp[i]).
        # Thus, replace:
        #   - dp[i-1] → prev
        #   - dp[i]   → curr
        # This reduces space from O(n1 * n2) to O(2 * n2)
        # ------------------------------------------------------------

        curr, prev = [0] * (n2 + 1), [0] * (n2 + 1)

        # Fill the table row by row using only two 1D arrays
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match → take diagonal value + 1
                    curr[j] = 1 + prev[j - 1]
                else:
                    # No match → max of top and left values
                    curr[j] = max(prev[j], curr[j - 1])

            # After finishing the current row, update prev to be curr
            prev = curr[:]

        # Final answer is in the last filled row, last column
        return prev[n2]

# ------------------------------------------------------------
# 🧠 Intuition:
# At any point, we only care about the previous row (i-1)
# and current row (i), so we can reduce the 2D table to two 1D arrays.

# We calculate LCS using:
# If match:     curr[j] = 1 + prev[j-1]
# If not match: curr[j] = max(prev[j], curr[j-1])

# prev → represents dp[i-1]
# curr → represents dp[i]
# ------------------------------------------------------------

# ⏱ Time Complexity: O(n1 * n2)
# 💾 Space Complexity: O(n2)
# Only two arrays of size n2 are maintained.
# ------------------------------------------------------------
