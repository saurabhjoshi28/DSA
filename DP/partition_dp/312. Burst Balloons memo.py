class Solution:
    def func(self, i, j, nums, dp):
        # Base case: No balloons to burst in this range
        if i > j:
            return 0

        # If already computed, return the stored result
        if dp[i][j] != -1:
            return dp[i][j]

        # Initialize the maximum coins for the current subproblem
        maxi = float('-inf')

        # Try each balloon from i to j as the last one to burst in this segment
        for k in range(i, j + 1):
            # Step 1: Burst balloon k last in the range [i...j]
            # Gain from bursting k depends on its neighbors: nums[i-1] and nums[j+1]
            coins = nums[i - 1] * nums[k] * nums[j + 1]

            # Step 2: Recursively calculate max coins for left and right segments
            left_coins = self.func(i, k - 1, nums, dp)
            right_coins = self.func(k + 1, j, nums, dp)

            # Step 3: Total coins = current burst + left + right
            total = coins + left_coins + right_coins

            # Step 4: Update maximum coins
            maxi = max(maxi, total)

        # Memoize and return
        dp[i][j] = maxi
        return dp[i][j]

    def maxCoins(self, nums: List[int]) -> int:
        """
        ========================
        Partition DP - Intuition
        ========================

        n balloons are given, each with a number.
        Bursting the i-th balloon gives coins = nums[i-1] * nums[i] * nums[i+1].

        Goal: Burst all balloons in an order that maximizes total coins.

        Why Partition DP?
        - The result depends on which balloon we burst last in a subarray.
        - Once the last balloon is chosen, the problem splits into two independent subproblems.

        Rules to solve using Partition DP:
        1. Start with the whole block [i...j] and try all possible partitions.
        2. For each position k in [i...j], assume it's the last balloon to burst.
        3. Calculate coins gained, solve left and right recursively, and take the maximum.
        """

        # Step 1: Pad nums with 1 at both ends to handle edge cases (virtual balloons)
        nums = [1] + nums + [1]

        n = len(nums)  # New length after padding

        # Step 2: Initialize DP table for memoization with -1
        dp = [[-1] * n for _ in range(n)]

        # Step 3: Call the recursive function on the real problem space (excluding padding)
        return self.func(1, n - 2, nums, dp)
