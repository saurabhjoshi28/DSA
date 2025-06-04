"""
===============================================================================
Palindrome Partitioning II – Memoization (Top-Down DP)
===============================================================================

Problem Statement
-----------------
Given a string s, partition it such that every substring of the partition is a palindrome.
Return the **minimum number of cuts** needed to make such a partition.

Intuition
---------
We try to place partitions (cuts) such that each substring becomes a palindrome.
Using recursion, we try all possible cuts starting at each index, and choose the one
with the **minimum number of total cuts**.

In this version, we use **memoization** to store already computed results
for each index `i`, where `dp[i]` stores the **minimum number of cuts** required
starting from index `i`.

Approach
--------
1. Define a recursive function `func(i)` that returns the minimum cuts needed for substring s[i:].
2. For every index `j` from `i` to `n-1`, check if s[i..j] is a palindrome.
   - If yes, make a cut and recursively solve the right substring s[j+1:].
   - Track the **minimum** of such partitions.
3. Use a DP array `dp` to memoize the result at each index `i`.

Base Case
---------
- If i == n → Reached the end of the string → no more cuts needed → return 0.

Memoization
-----------
- If dp[i] is already computed, return it to avoid recomputation.

Final Result Adjustment
-----------------------
We subtract 1 from the final result because an extra cut is added after the last character.

Time Complexity
---------------
O(N^2) for checking all substring partitions, assuming palindrome checking is constant
due to substring slicing (not optimal, can be improved with precomputation).

===============================================================================
"""

class Solution:
    def ispal(self, x):
        # Helper function to check if a string is a palindrome
        return x == x[::-1]

    def func(self, i, n, s, dp):
        # Base Case: No more characters to cut
        if i == n:
            return 0

        # Return cached result if already computed
        if dp[i] != -1:
            return dp[i]

        mini = float('inf')
        # Try all partitions starting from index i to n-1
        for j in range(i, n):
            # If substring s[i..j] is palindrome, try cutting here
            if self.ispal(s[i:j+1]):
                # Cost is 1 (cut) + minimum cuts for the right substring
                cost = 1 + self.func(j + 1, n, s, dp)
                mini = min(mini, cost)  # Track minimum cuts

        # Memoize and return the result
        dp[i] = mini
        return dp[i]

    def minCut(self, s: str) -> int:
        n = len(s)
        s = list(s)  # Convert string to list for slicing convenience
        dp = [-1] * n  # Initialize DP array
        return self.func(0, n, s, dp) - 1  # Subtract 1 to correct extra cut
