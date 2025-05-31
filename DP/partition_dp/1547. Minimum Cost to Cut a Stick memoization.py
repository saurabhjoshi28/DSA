class Solution:
    def func(self, i , j, cuts, dp):
        # Base case: If the segment has no cuts to be made (i > j), return 0 cost.
        if j < i:
            return 0

        # Memoization check: if we already have a result stored for this segment, return it.
        if dp[i][j] != -1:
            return dp[i][j]

        # Initialize minimum cost as infinity
        mini = float('inf')

        # Try placing a cut at every position from i to j
        for k in range(i, j + 1):
            # Step 1: Cost of cutting at cuts[k] is the length of the current stick segment.
            # That is, distance between cuts[j+1] and cuts[i-1].
            cost_of_cut = cuts[j + 1] - cuts[i - 1]

            # Step 2: Solve left and right subproblems recursively
            # Left: cuts[i] to cuts[k-1]
            left_cost = self.func(i, k - 1, cuts, dp)

            # Right: cuts[k+1] to cuts[j]
            right_cost = self.func(k + 1, j, cuts, dp)

            # Step 3: Total cost = cost of this cut + left + right subproblem costs
            total_cost = cost_of_cut + left_cost + right_cost

            # Step 4: Update minimum cost if this configuration gives a better answer
            mini = min(mini, total_cost)

        # Memoize and return the minimum cost found
        dp[i][j] = mini
        return dp[i][j]

    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        ========================
        Partition DP - Intuition
        ========================

        Whenever the order of solving the problem comes into play,
        we can think in terms of Partition DP.

        Rules to solve using Partition DP:
        1. Start with the entire block/array and mark it with i, j.
        2. Try all partitions between i and j.
        3. Return the best possible answer (usually the minimum/maximum)
           after solving the two partitions recursively.
        """

        # Step 1: Sort the cuts to ensure correct partitioning
        cuts.sort()

        # Step 2: Add 0 and n to the start and end of the cuts list respectively
        # This helps in computing the cost of the outermost segment (entire stick)
        cuts = [0] + cuts + [n]

        # Step 3: Length of updated cuts list
        m = len(cuts)

        # Step 4: Initialize DP table with -1 for memoization
        dp = [[-1] * m for _ in range(m)]

        # Step 5: Call the recursive memoized function from index 1 to m-2
        # We skip 0 and n because those are added boundaries
        return self.func(1, m - 2, cuts, dp)
