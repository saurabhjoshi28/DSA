class Solution:
    def func(self, i, j, nums):
        # Base case: If the range is invalid (no balloons to burst), return 0
        if i > j:
            return 0

        # Initialize maximum coins collected for this subproblem
        maxi = float('-inf')

        # Try bursting each balloon from i to j as the last balloon in this range
        for k in range(i, j + 1):
            # Step 1: Coins from bursting the k-th balloon last in the current segment
            # The gain from bursting balloon k is:
            # nums[i-1] * nums[k] * nums[j+1]
            # because nums[i-1] and nums[j+1] are adjacent once all between i and j are popped
            coins = nums[i - 1] * nums[k] * nums[j + 1]

            # Step 2: Recursively solve the left and right subproblems
            left_coins = self.func(i, k - 1, nums)
            right_coins = self.func(k + 1, j, nums)

            # Step 3: Total coins if we burst balloon k last
            total = coins + left_coins + right_coins

            # Step 4: Update maximum coins collected
            maxi = max(maxi, total)

        # Return the maximum coins that can be collected in range [i, j]
        return maxi

    def maxCoins(self, nums: List[int]) -> int:
        """
        ========================
        Partition DP - Intuition
        ========================

        n balloons are given (indexed from 0 to n-1), each with a number.
        Bursting the i-th balloon yields coins = nums[i-1] * nums[i] * nums[i+1]
        We aim to burst all balloons to maximize the total coins.

        Note:
        - After a balloon bursts, its neighbors become adjacent.
        - Hence, the order of bursting matters => Partition DP.

        Partition DP Rules:
        1. Define the entire problem with a range [i, j].
        2. Try every possible "last burst" within that range.
        3. Recursively compute left and right partitions.
        4. Return the maximum coins from all such configurations.
        """

        # Step 1: Add 1 at both ends for edge calculations (virtual balloons)
        nums = [1] + nums + [1]

        n = len(nums)  # Updated size after padding

        # Step 2: Start the recursive computation from index 1 to n-2 (ignore virtual ends)
        return self.func(1, n - 2, nums)
