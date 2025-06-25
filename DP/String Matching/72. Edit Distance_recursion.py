class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        # 🔍 Intuition:
        # This is the classic Edit Distance (Levenshtein Distance) problem.
        # We need to convert word1 into word2 using the minimum number of operations.
        # Allowed operations are:
        # 1. Insert a character
        # 2. Delete a character
        # 3. Replace a character

        # Let func(i, j) represent the minimum number of operations needed
        # to convert word1[0..i] to word2[0..j]

        # Base Cases:
        # If i < 0, that means word1 is exhausted — so we must insert (j+1) characters from word2.
        # If j < 0, that means word2 is exhausted — so we must delete (i+1) characters from word1.

        def func(i, j):
            if i < 0:
                return j + 1  # Insert remaining characters of word2
            if j < 0:
                return i + 1  # Delete remaining characters of word1

            # If characters match, we move both pointers without any operation
            if word1[i] == word2[j]:
                return func(i - 1, j - 1)

            # If characters do not match, we have three choices:

            # 🔁 Insert: match word1[0..i] with word2[0..j-1], and insert word2[j] → cost +1
            insert = 1 + func(i, j - 1)

            # ❌ Delete: delete word1[i], now match word1[0..i-1] with word2[0..j] → cost +1
            delete = 1 + func(i - 1, j)

            # 🔁 Replace: replace word1[i] with word2[j], then move both → cost +1
            replace = 1 + func(i - 1, j - 1)

            # Return minimum among all three operations
            return min(insert, delete, replace)

        return func(n1 - 1, n2 - 1)
