class Solution:
    def func(self, i , j, cuts):
        # Base case: If there are no cuts to be made in the current segment (i > j),
        # the cost is 0, since no cutting is needed.
        if j < i:
            return 0

        # Initialize minimum cost to infinity.
        # We'll try all possible cut points from i to j and select the one
        # that gives us the minimum cost.
        mini = float('inf')

        # Try placing a cut at every possible position k between i and j
        for k in range(i, j + 1):
            # Step 1: Calculate the cost of making a cut at position cuts[k]
            # The cost of making this cut is equal to the length of the current stick segment,
            # which is given by cuts[j+1] - cuts[i-1]
            cost_of_cut = cuts[j + 1] - cuts[i - 1]

            # Step 2: Recursively calculate the cost for left and right subsegments
            # - Left subproblem: cuts between i and k-1
            # - Right subproblem: cuts between k+1 and j
            left_cost = self.func(i, k - 1, cuts)
            right_cost = self.func(k + 1, j, cuts)

            # Total cost = cost to make this cut + cost to solve subproblems
            total_cost = cost_of_cut + left_cost + right_cost

            # Take the minimum over all possible cuts
            mini = min(mini, total_cost)

        # Return the minimum cost to cut the stick between cuts[i-1] and cuts[j+1]
        return mini

    def minCost(self, n: int, cuts: List[int]) -> int:
        # -----------------------------------------------
        # Whenever the order of solving the problem comes into play,
        # we can think in terms of Partition DP.
        # -----------------------------------------------

        # Step 1: Sort the cuts array.
        # This ensures that when we try to cut at a position,
        # the left and right parts have their correct cuts within their own subproblems.
        cuts.sort()

        # Step 2: Insert 0 at the beginning and n at the end of the cuts list.
        # This represents the full stick boundaries.
        cuts = [0] + cuts + [n]

        # Step 3: Define the total number of cuts (including 0 and n)
        m = len(cuts)

        # Step 4: Call the recursive function to find the minimum cost to cut
        # from the first actual cut (index 1) to the last one (index m - 2)
        return self.func(1, m - 2, cuts)