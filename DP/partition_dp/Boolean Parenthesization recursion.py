"""
===============================================================================
Boolean Parenthesization – Recursive / Partition DP Approach
===============================================================================

Problem Statement
-----------------
Given a boolean expression with symbols:
- 'T' (true), 'F' (false)
- Operators: AND (&), OR (|), XOR (^)

We need to count the number of ways to parenthesize the expression such that
it evaluates to **True**.

Why Use Partition DP?
---------------------
This is a Partition DP problem because:
- We partition the expression at each operator (which lies at odd indices),
- Compute results for left and right sub-expressions independently,
- Then combine the sub-results based on the operator.

Function Signature
------------------
func(i, j, isTrue, s): Returns number of ways to evaluate expression s[i..j]
to result `isTrue`.

Base Cases
----------
- If i > j: return 0 (invalid expression)
- If i == j: return 1 if s[i] matches expected boolean, else 0

Recursive Case
--------------
- Loop through each operator `k` from i+1 to j with step of 2
  (operators are at odd indices).
- Split into left (i to k-1) and right (k+1 to j)
- Recursively compute:
    LT = ways left side evaluates to True
    LF = ways left side evaluates to False
    RT = ways right side evaluates to True
    RF = ways right side evaluates to False

Operator Logic
--------------
If s[k] is:
- '&':
    isTrue => LT * RT
    isFalse => LT*RF + LF*RT + LF*RF
- '|':
    isTrue => LT*RT + LT*RF + LF*RT
    isFalse => LF * RF
- '^':
    isTrue => LT*RF + LF*RT
    isFalse => LT*RT + LF*RF

Time and Space Complexity
-------------------------
- States: O(N^2 * 2) => O(N^2)
- Transitions: O(N) per state => Overall: O(N^3)
- No memoization used here (can be added for optimization)

===============================================================================
"""

# User function Template for python3
class Solution:
    def func(self, i, j, isTrue, s):
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

        ways = 0
        for k in range(i + 1, j, 2):
            LT = self.func(i, k - 1, True, s)
            LF = self.func(i, k - 1, False, s)
            RT = self.func(k + 1, j, True, s)
            RF = self.func(k + 1, j, False, s)

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

        return ways
        
    def countWays(self, s):
        s = list(s)
        n = len(s)
        return self.func(0, n - 1, True, s)
