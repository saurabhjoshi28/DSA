from typing import List

class Solution:
    def is_one_extra_char(self, s1, s2):
        """
        Helper function to check if inserting exactly one character in s1 makes it equal to s2.
        This is similar to checking the "next element" condition in a typical LIS problem.
        """
        if len(s1) > len(s2):
            s1, s2 = s2, s1  # Ensure s1 is the shorter word

        # Early exit if length difference is not exactly 1
        if len(s2) - len(s1) != 1:
            return False

        i, j = 0, 0
        mismatch_found = False

        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                if mismatch_found:
                    return False
                mismatch_found = True
                j += 1  # Skip the extra character in s2

        return True  # Valid if only one mismatch (insertion) occurred

    def longestStrChain(self, words: List[str]) -> int:
        """
        Main function to find the length of the longest string chain.

        Concept:
        --------
        This is a variation of the Longest Increasing Subsequence (LIS) problem.
        - In LIS, we compare numbers to find increasing sequences.
        - Here, instead of numbers, we compare words.
        - One word comes after another in the chain if it can be formed by inserting
          exactly one character in the previous word.
        
        Approach:
        ---------
        1. Sort the words by their lengths (similar to sorting numbers in LIS).
        2. Use DP where dp[i] stores the length of the longest chain ending at words[i].
        3. For each word[i], check all previous word[prev] and apply LIS-style transition
           if word[i] is a valid successor of word[prev].

        Time Complexity: O(N^2 * L) where L is average word length (due to helper function).
        """
        n = len(words)
        words.sort(key=lambda x: len(x))  # Sorting based on length (LIS setup)

        dp = [1] * n  # dp[i] represents longest chain ending at words[i]
        max_lis = 1   # Will hold the max value of the chain

        for i in range(n):
            for prev in range(i):
                if self.is_one_extra_char(words[prev], words[i]):
                    if dp[i] < 1 + dp[prev]:
                        dp[i] = 1 + dp[prev]
                    max_lis = max(max_lis, dp[i])

        return max_lis
