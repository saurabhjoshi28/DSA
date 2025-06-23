class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Let n1 = length of word1, n2 = length of word2
        n1, n2 = len(word1), len(word2)

        """
        💡 Intuition:
        This problem is about finding the **minimum number of operations** 
        (insertion, deletion) to convert one string into another.

        ✅ Key Insight:
        We can convert both strings into their **Longest Common Subsequence (LCS)** 
        by deleting characters from either side.

        So, the total number of operations = 
            (number of deletions in word1) + (number of deletions in word2)

        → Deletions in word1 = n1 - LCS
        → Deletions in word2 = n2 - LCS

        🔁 Therefore, total operations = (n1 - LCS) + (n2 - LCS) = n1 + n2 - 2 * LCS
        """

        # Recursive LCS function
        def func(i, j):
            # Base case: if either pointer goes out of bounds
            if i < 0 or j < 0:
                return 0
            # If characters match, move diagonally and add 1
            if word1[i] == word2[j]:
                return 1 + func(i - 1, j - 1)
            # Else, move in both directions and take max
            return max(func(i - 1, j), func(i, j - 1))

        # Step 1: Find LCS between word1 and word2
        lcs = func(n1 - 1, n2 - 1)

        # Step 2: Use the formula: min operations = n1 + n2 - 2 * LCS
        return n1 + n2 - (2 * lcs)

# ----------------------------------------------
# 🔍 Example:
# word1 = "sea", word2 = "eat"
# LCS = "ea" → len = 2
# Operations = 3 + 3 - 2*2 = 6 - 4 = 2
# One valid sequence: "sea" → delete 's' → "ea" → insert 't' → "eat"
# ----------------------------------------------

# ❗ Note: This is the recursive version. Time complexity is exponential (O(2^n)).
# ✅ You can optimize it using memoization or tabulation to make it O(n^2).
