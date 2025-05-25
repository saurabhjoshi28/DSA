class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Approach: 1D Dynamic Programming (Tabulation)

        - We maintain a dp array where dp[i] represents the length of the Longest Increasing Subsequence (LIS)
          that ends at index `i`.
        - For each index `i`, we check all previous indices `j` (0 <= j < i), and if nums[j] < nums[i],
          it means nums[i] can extend the LIS ending at nums[j].
        - So we update dp[i] = max(dp[i], 1 + dp[j])
        - Finally, the maximum value in the dp array is the length of the overall LIS.

        Example:
        nums = [5, 4, 11, 1, 16, 8]
        dp explanation:
            dp[0] = 1 → LIS ending at 5 is just [5]
            dp[1] = 1 → LIS ending at 4 is [4]
            dp[2] = 2 → [5,11] or [4,11]
            dp[3] = 1 → [1]
            dp[4] = 3 → [5,11,16] or [4,11,16]
            dp[5] = 2 → [5,8] or [1,8]
        Final answer = max(dp) = 3
        """

        n = len(nums)
        
        # Initialize all LIS lengths as 1 (every element is a subsequence of length 1)
        dp = [1] * n

        # Track the overall maximum LIS
        max_lis = 1

        for i in range(n):
            for prev in range(i):
                if nums[prev] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[prev])

            # Update global maximum LIS length
            max_lis = max(max_lis, dp[i])

        return max_lis