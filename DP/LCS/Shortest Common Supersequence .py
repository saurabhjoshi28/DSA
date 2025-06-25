class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        💡 Intuition:
        We are given two strings `str1` and `str2`, and we need to create the **shortest string**
        that has both `str1` and `str2` as subsequences.

        ⚠️ Observation:
        If we simply concatenate both strings, we will definitely get a supersequence,
        but not necessarily the *shortest*. To make it shortest, we must avoid repeating the
        common parts.

        🔑 Key Insight:
        The **Longest Common Subsequence (LCS)** is the overlap part between str1 and str2.
        So the shortest common supersequence (SCS) length will be:
            len(SCS) = len(str1) + len(str2) - len(LCS)
        
        🎯 Goal:
        We don’t just want the length, we need the actual **string**.
        So, we do:
        - Step 1: Find the LCS using standard DP.
        - Step 2: Backtrack from dp[n1][n2] and build the result string by merging both,
          while preserving the order of characters.
        """

        n1, n2 = len(str1), len(str2)

        # Step 1: Create LCS dp table (standard)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 2: Backtrack to build the shortest common supersequence
        i, j = n1, n2
        res = []

        while i > 0 and j > 0:
            # If characters match, this char is part of LCS (and hence SCS), include it
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            # If not, follow the direction which gave max value in LCS table
            elif dp[i - 1][j] > dp[i][j - 1]:
                res.append(str1[i - 1])  # Include str1 char first
                i -= 1
            else:
                res.append(str2[j - 1])  # Include str2 char first
                j -= 1

        # If any characters are left in str1 or str2 (not part of LCS), append them
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        # The result is built in reverse, so reverse it before returning
        return ''.join(res[::-1])


"""
🧠 Dry-run Example:
str1 = "abac"
str2 = "cab"

LCS = "ab" or "ac" → suppose "ab"

Then, while backtracking:
- Merge 'c' from str2 (before 'a')
- Add 'a' (common)
- Add 'b' (common)
- Add 'c' from str1 (after 'b')

Result = "cabac"

✅ Time Complexity: O(n1 * n2)
✅ Space Complexity: O(n1 * n2) for DP table
"""
