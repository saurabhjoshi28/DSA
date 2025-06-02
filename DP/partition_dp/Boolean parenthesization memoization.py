"""
===============================================================================
Boolean Parenthesization – Memoized Recursive (Top-Down DP)
===============================================================================

Problem Statement
-----------------
Given a boolean expression with symbols:
- 'T' (true), 'F' (false)
- Operators: AND (&), OR (|), XOR (^)

Goal:
Count the number of ways to parenthesize the expression such that
the result is **True**.

Why Partition DP?
-----------------
This problem involves recursively splitting the expression at each operator,
evaluating left and right sub-expressions independently, and combining
them based on the operator's logic.

Memoization Optimization
------------------------
We use memoization to avoid recalculating overlapping subproblems.
The DP table is a 3D list: dp[i][j][isTrue]
- i and j define the substring range
- isTrue is a boolean (0/1) indicating the expected result

States:
- (i, j, isTrue) → number of ways s[i..j] evaluates to isTrue

Base Cases
----------
- If i > j → invalid range → return 0
- If i == j → directly compare s[i] to isTrue ('T' or 'F')

Recursive Case
--------------
Loop through every operator k (odd indices):
- Recursively calculate:
    LT = ways left side (i to k-1) is True
    LF = ways left side is False
    RT = ways right side (k+1 to j) is True
    RF = ways right side is False

Combine according to operator:
- '&':
    isTrue: ways += LT * RT
    isFalse: ways += LT*RF + LF*RT + LF*RF
- '|':
    isTrue: ways += LT*RT + LT*RF + LF*RT
    isFalse: ways += LF * RF
- '^':
    isTrue: ways += LT*RF + LF*RT
    isFalse: ways += LT*RT + LF*RF

Time and Space Complexity
-------------------------
- Time: O(N^3) due to partitioning and memoization (N = length of expression)
- Space: O(N^2 * 2) for 3D DP table

===============================================================================
"""

# User function Template for python3
class Solution:
    def func(self, i, j, isTrue, s, dp):
        if i > j:
            return 0
        if i == j:
            if isTrue:
                if s[i] == 'T':
                    return 1
                else:
                    return 0
            else: 
                if s[i] == 'F':
                    return 1
                else:
                    return 0

        if dp[i][j][isTrue] != -1:
            return dp[i][j][isTrue]

        ways = 0
        for k in range(i + 1, j, 2):
            LT = self.func(i, k - 1, True, s, dp)
            LF = self.func(i, k - 1, False, s, dp)
            RT = self.func(k + 1, j, True, s, dp)
            RF = self.func(k + 1, j, False, s, dp)

            if s[k] == '&':
                if isTrue:
                    ways += LT * RT
                else:
                    ways += (LT * RF) + (LF * RT) + (LF * RF)
            elif s[k] == '|':
                if isTrue:
                    ways += (LT * RT) + (LT * RF) + (LF * RT)
                else:
                    ways += (LF * RF)
            else:
                if isTrue:
                    ways += (LT * RF) + (LF * RT)
                else:
                    ways += (LT * RT) + (LF * RF)

        dp[i][j][isTrue] = ways
        return dp[i][j][isTrue]

    def countWays(self, s):
        s = list(s)
        n = len(s)
        dp = [[[-1] * 2 for _ in range(n)] for _ in range(n)]
        return self.func(0, n - 1, True, s, dp)
