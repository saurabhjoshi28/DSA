class Solution:
    def minInsertions(self, s: str) -> int:
        # s1 = original string
        # s2 = reverse of the original string
        s1, s2 = s, s[::-1]
        n1, n2 = len(s1), len(s2)

        """
        🧠 Intuition:
        To make a string palindrome with the **minimum number of insertions**, 
        we want to **retain as much of its existing palindromic structure as possible**.

        So, we first compute the **Longest Palindromic Subsequence (LPS)** in the string.
        Once we know the LPS, the characters **not in** the LPS are the ones we need to insert
        (in mirrored positions) to make the full string a palindrome.

        🔍 Observation:
        Minimum insertions required = Total length - Length of LPS

        Why?
        Because the LPS already forms a part of the palindrome, and the rest
        must be mirrored by inserting characters.
        """

        # Classic recursive LCS function between original and its reverse
        def func(i, j):
            # Base case: when either index goes out of bound
            if i < 0 or j < 0:
                return 0
            # If characters match, count it and move diagonally
            if s1[i] == s2[j]:
                return 1 + func(i - 1, j - 1)
            # If they don't match, skip one character from either string
            return max(func(i, j - 1), func(i - 1, j))

        # Find length of Longest Palindromic Subsequence
        lps = func(n1 - 1, n2 - 1)

        # Result = characters not in LPS (i.e. need to be inserted)
        return n1 - lps

# --------------------------------------------
# 🔍 Example: s = "mbadm"
# s[::-1] = "mdabm"
# LPS = "madam" → lps = 3
# Insertions needed = 5 - 3 = 2
# We can insert 2 characters to make it palindrome → "mbdadbm"
# --------------------------------------------

# ✅ Time Complexity: O(2^n) in this recursive version (exponential)
# ⚠️ You can optimize it with memoization (DP) to O(n^2)
# ✅ Space Complexity: O(n) recursion stack
