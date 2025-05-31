"""
=======================
Partition DP - Intuition
=======================

Let us quickly revise the rules to solve a problem using Partition DP:

1. Start with the entire block/array and mark it with i, j.
2. Try all possible partitions between i and j.
3. Return the best possible answer among all the partitions.
   (This is typically the answer obtained by dividing the problem 
   into two subproblems and solving them recursively.)

Whenever the **order of solving the problem** comes into play,
we can think in terms of **Partition DP**.

This pattern is commonly applied in problems such as:
- Matrix Chain Multiplication
- Minimum Cost to Cut a Stick
- Palindrome Partitioning
- Burst Balloons

In most of these, you're trying to find the optimal cost/result 
of splitting or combining segments of an array using recursion 
+ memoization or bottom-up DP.
"""
