class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Intuition:
        # A palindromic subsequence is just a sequence that reads the same forwards and backwards,
        # but **it doesn't need to be contiguous**.

        # Example: s = "bbabcbcab"
        # One of the longest palindromic subsequences: "babcbab" → length = 7

        # 🧠 Key Idea:
        # If we reverse the string, and then compute the Longest Common Subsequence (LCS)
        # between the original string and its reverse, the LCS will be the longest palindromic subsequence.
        #
        # Why?
        # Because a palindrome reads the same forwards and backwards,
        # so the subsequence which is common between the string and its reverse
        # will be a palindrome.

        s1, s2 = s, s[::-1]  # s2 is the reverse of s1
        n1, n2 = len(s1), len(s2)

        # Recursive helper function to calculate LCS of s1 and s2
        def func(i, j):
            # Base case: if either index goes negative, no subsequence can be formed
            if i < 0 or j < 0:
                return 0
            # If characters match, include this character in the count
            if s1[i] == s2[j]:
                return 1 + func(i - 1, j - 1)
            # If not matching, try both possibilities and take max
            return max(func(i, j - 1), func(i - 1, j))

        return func(n1 - 1, n2 - 1)

# -----------------------------------------
# 🔍 Example: s = "agbdba"
# Reversed: s[::-1] = "abdbga"
# LCS("agbdba", "abdbga") = "abdba" → length = 5
# So, longest palindromic subsequence = 5
# -----------------------------------------

# ✅ Time Complexity (Recursive without memo): Exponential, due to overlapping subproblems
# ✅ Space Complexity: O(n1 + n2) recursion stack
