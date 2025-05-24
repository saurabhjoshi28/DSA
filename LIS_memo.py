class Solution:
    def func(self, i, prev, nums, dp):
        n = len(nums)

        # Base case: if we've reached the end of the array
        if i == n:
            return 0
        
        # If it's already solved, use memoized value
        if dp[i][prev + 1] != -1:
            return dp[i][prev + 1]

        pick = float('-inf')

        # If we can pick the current element to be part of the increasing subsequence
        if prev == -1 or nums[prev] < nums[i]:
            pick = 1 + self.func(i+1, i, nums, dp)

        # Explore the option of not picking the current element
        notpick = 0 + self.func(i+1, prev, nums, dp)

        # Memoize the result
        dp[i][prev + 1] = max(pick, notpick)

        return dp[i][prev + 1]


    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Optimized using memoization:
        - Use recursion to explore all subsequences.
        - Memoize the overlapping subproblems.
        - The function `func(i, prev, nums, dp)` computes LIS starting at index `i`
          with the last picked index being `prev`.
        """
        n = len(nums)

        # dp[i][prev+1] is used to shift -1 to 0-indexed for valid access
        dp = [[-1] * (n + 1) for _ in range(n)]
        return self.func(0, -1, nums, dp)