"""
===============================================================================
Palindrome Partitioning II – Tabulation (Bottom-Up DP)
===============================================================================

Intuition
---------
Instead of solving the problem top-down (recursively), we build the solution
from the back of the string toward the front. For every index `i`, we determine the
minimum number of cuts required to partition the substring s[i:] such that each part is a palindrome.

Approach
--------
1. We define a 1D array `dp` of size (n+1), where dp[i] represents the minimum cuts
   needed to partition the substring s[i:].
2. Start from the last index and move backwards to 0.
3. For each index `i`, try every possible end index `j` from `i` to `n-1`.
   - If s[i:j+1] is a palindrome, compute the cost of making a cut after j and use dp[j+1] for the right part.
   - Add 1 for the cut made after the palindrome s[i:j+1].
4. Store the minimum cost in dp[i].
5. Finally, return dp[0] - 1 because one extra cut is counted after the last character.

Time Complexity
---------------
- O(N^3) in worst case because:
  - For each index i, we try all j from i to n (O(N^2)),
  - And for each s[i:j+1], we check if it's a palindrome in O(N).

Space Complexity
----------------
- O(N) for the dp array.

Optimizations
-------------
- Palindrome checking can be optimized using a precomputed 2D boolean table.

===============================================================================
"""

class Solution:
    def ispal(self, x):
        # Helper function to check if a string is palindrome using two pointers
        i, j = 0, len(x) - 1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True

    def minCut(self, s: str) -> int:
        n = len(s)

        # Edge case: if entire string is already a palindrome, return 0 cuts needed
        if self.ispal(s):
            return 0

        # dp[i] = min number of cuts needed for s[i:]
        dp = [0] * (n + 1)  # Initialize dp array of size n+1

        # Fill dp[] from back to front
        for i in range(n - 1, -1, -1):
            mini = float('inf')
            for j in range(i, n):
                if self.ispal(s[i:j + 1]):
                    # 1 cut after s[i:j], then solve for s[j+1:]
                    cost = 1 + dp[j + 1]
                    mini = min(mini, cost)
            dp[i] = mini

        return dp[0] - 1  # Subtract 1 due to extra final cut
