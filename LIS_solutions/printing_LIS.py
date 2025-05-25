from typing import List

def printingLongestIncreasingSubsequence(arr: List[int], n: int) -> List[int]:
    """
    Function to return the actual Longest Increasing Subsequence (LIS) in the given array.

    Approach:
    - dp[i] stores the length of the LIS ending at index i.
    - backtrack[i] stores the index of the previous element in the LIS that ends at i.
    - After filling dp[] and backtrack[], we find the index where LIS ends (max length),
      and then reconstruct the subsequence by backtracking from that index.

    Example:
    arr = [5, 4, 11, 1, 16, 8]
    LIS  = [5, 11, 16] ? reconstructed using the backtrack array.
    """

    n = len(arr)
    
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * n

    # backtrack[i] stores the index of the previous element in the LIS ending at i
    backtrack = [i for i in range(n)]

    max_lis = 1          # Length of longest LIS found so far
    last_index = 0       # Index at which LIS ends

    for i in range(n):
        for prev in range(i):
            if arr[prev] < arr[i] and dp[i] < 1 + dp[prev]:
                dp[i] = 1 + dp[prev]
                backtrack[i] = prev

        if dp[i] > max_lis:
            max_lis = dp[i]
            last_index = i

    # Reconstruct the LIS by backtracking from the last index
    lis_sequence = []
    lis_sequence.append(arr[last_index])
    current = last_index

    while backtrack[current] != current:
        current = backtrack[current]
        lis_sequence.append(arr[current])

    # Since we collected elements from end to start, reverse it
    return lis_sequence[::-1]
    