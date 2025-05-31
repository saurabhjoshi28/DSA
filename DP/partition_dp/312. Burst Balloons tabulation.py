class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        ==========================
        Partition DP (Tabulation)
        ==========================

        Problem Summary:
        - Given n balloons, each with a number in nums.
        - Bursting balloon `i` gives `nums[i-1] * nums[i] * nums[i+1]` coins.
        - After a balloon is burst, its neighbors become adjacent.
        - We need to burst all balloons in an order that maximizes total coins.

        Tabulation Plan:
        - We previously defined dp[i][j] as the max coins from bursting all balloons in the range [i, j].
        - Base case: if i > j, there are no balloons to burst ⇒ dp[i][j] = 0.
        - Try every `k` in [i, j] as the last balloon to burst in that range:
            - Coins gained = nums[i-1] * nums[k] * nums[j+1]
            - Total = coins gained + dp[i][k-1] + dp[k+1][j]
            - Take max over all possible `k`.
        - Build the dp table in increasing order of subarray size.
        """

        # Step 1: Pad nums with 1 at both ends to handle edge balloons
        nums = [1] + nums + [1]

        n = len(nums)  # Total length including padding

        # Step 2: Initialize a 2D dp table
        dp = [[0] * (n + 2) for _ in range(n + 2)]  # Extra space for safety

        # Step 3: Fill the dp table from shorter to longer subarrays
        for i in range(n - 2, 0, -1):  # Start from the end towards the start
            for j in range(1, n - 1):  # Go from left to right
                if i > j:
                    continue  # Invalid range, skip

                # Step 4: Try every balloon in range [i, j] as the last to burst
                maxi = float('-inf')
                for k in range(i, j + 1):
                    coins = (
                        nums[i - 1] * nums[k] * nums[j + 1]  # Burst k last
                        + dp[i][k - 1]                       # Left subproblem
                        + dp[k + 1][j]                       # Right subproblem
                    )
                    maxi = max(maxi, coins)

                # Step 5: Store the best result in dp[i][j]
                dp[i][j] = maxi

        # Step 6: Return the max coins from bursting all real balloons (excluding virtual ones)
        return dp[1][n - 2]
