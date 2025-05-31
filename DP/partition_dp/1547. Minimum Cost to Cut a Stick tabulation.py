class Solution:
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

        # Step 1: Sort the cuts to process them in logical left-to-right order
        cuts.sort()

        # Step 2: Add boundaries 0 and n to the cuts list
        # This helps simplify the cost computation for edge segments
        c = len(cuts)
        cuts = [0] + cuts + [n]

        # Step 3: Initialize the DP table
        # dp[i][j] will represent the minimum cost to cut the stick between cuts[i-1] and cuts[j+1]
        dp = [[0] * (c + 2) for _ in range(c + 2)]

        # Step 4: Fill the table bottom-up
        # We try all possible segment lengths starting from smaller to larger
        for i in range(c, 0, -1):  # Start from the end and move backwards for i
            for j in range(1, c + 1):  # j must be ahead of i
                if i > j:
                    continue  # No cuts to be made in this segment

                # Step 5: Try all possible cut positions between i and j
                mini = float('inf')
                for k in range(i, j + 1):
                    # Cost of cutting between cuts[i-1] and cuts[j+1]
                    cost_of_cut = cuts[j + 1] - cuts[i - 1]

                    # Left and right subproblems already computed
                    left_cost = dp[i][k - 1]
                    right_cost = dp[k + 1][j]

                    # Total cost = cost of this cut + left + right
                    total_cost = cost_of_cut + left_cost + right_cost

                    # Update minimum
                    mini = min(mini, total_cost)

                # Store result in DP table
                dp[i][j] = mini

        # Step 6: Return the final result (minimum cost to cut from first to last actual cut)
        return dp[1][c]
