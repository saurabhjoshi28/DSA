from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Problem:
        Given a set of distinct positive integers `nums`, return the largest subset such that
        for every pair (i, j) in the subset, one element divides the other (i.e., nums[i] % nums[j] == 0).

        Approach: Similar to Longest Increasing Subsequence (LIS)
        ----------------------------------------------------------
        - In LIS, we look for sequences where nums[i] > nums[prev].
        - In this problem, instead of increasing order, we look for divisibility: nums[i] % nums[prev] == 0
        - We sort the array to ensure if nums[i] % nums[j] == 0, then i > j
        - Use DP to build the length of the largest divisible subset ending at each index (just like LIS)
        - Use a backtracking array to reconstruct the actual subset (also like LIS trace)

        Example:
        nums = [1, 2, 4, 8]
        LIS-style logic checks:
        - 2 % 1 == 0 → 2 can follow 1
        - 4 % 2 == 0 → 4 can follow 2
        - 8 % 4 == 0 → 8 can follow 4
        → Result = [1, 2, 4, 8]
        """

        n = len(nums)
        nums.sort()  # Sorting allows us to check only if nums[i] % nums[prev] == 0

        # dp[i]: length of largest divisible subset ending at index i
        dp = [1] * n

        # backtrack[i]: stores previous index in the subset chain ending at i
        backtrack = [i for i in range(n)]

        # Track the length and ending index of the longest subset found
        max_len = 1
        last_index = 0

        for i in range(n):
            for prev in range(i):
                # If divisible and adding nums[i] increases the subset length
                if nums[i] % nums[prev] == 0 and dp[i] < 1 + dp[prev]:
                    dp[i] = 1 + dp[prev]
                    backtrack[i] = prev

            # Update global max length and ending index
            if dp[i] > max_len:
                max_len = dp[i]
                last_index = i

        # Reconstruct the subset by following the backtrack chain
        result = []
        result.append(nums[last_index])
        current = last_index

        while backtrack[current] != current:
            current = backtrack[current]
            result.append(nums[current])

        return result[::-1]  # Reverse to get elements in increasing order
