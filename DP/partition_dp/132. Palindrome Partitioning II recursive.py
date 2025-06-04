"""
===============================================================================
Palindrome Partitioning II – Recursive Approach
===============================================================================

Problem Statement
-----------------
Given a string s, partition it such that every substring of the partition is a palindrome.
Return the **minimum number of cuts** needed to make such a partition.

Key Insight
-----------
It is always possible to partition a string into palindromic substrings by making n-1 cuts
(for a string of length n). But our goal is to **minimize** the number of such cuts.

Example:
---------
For s = "aabb", one valid palindromic partition is: "aa | b | b" → 2 cuts.

Approach
--------
This problem is solved using **front partition recursion**:

1. Start from index `i = 0`.
2. Try every partition point `j` from `i` to `n-1`.
3. For each substring s[i..j], if it's a palindrome, then:
   - Cut it
   - Recur on the rest of the string s[j+1..n-1]
   - Add 1 to the current cut
4. Track the minimum number of such valid cuts among all j

Base Case
---------
- If i == n (end of the string), no more cuts needed → return 0.

Final Result Adjustment
-----------------------
Since the function adds a cut after the last character unnecessarily,
we subtract 1 from the final result to correct it.

Time Complexity
---------------
- Exponential in worst case due to repeated calls without memoization.

===============================================================================
"""

class Solution:
    def ispal(self, x):
        # Helper function to check if a substring is a palindrome
        return x == x[::-1]

    def func(self, i, n, s):
        # Base Case: If we have reached the end of the string, no more cuts needed
        if i == n:
            return 0

        mini = float('inf')
        # Try partitioning from index i to every j in [i, n-1]
        for j in range(i, n):
            # If the current substring is a palindrome, consider cutting here
            if self.ispal(s[i:j+1]):
                # Recursively calculate cuts for the remaining substring
                cost = 1 + self.func(j + 1, n, s)
                # Track the minimum number of cuts
                mini = min(mini, cost)
        return mini

    def minCut(self, s: str) -> int:
        n = len(s)
        s = list(s)  # Convert string to list for slicing
        return self.func(0, n, s) - 1  # Subtract 1 to adjust for the extra cut
