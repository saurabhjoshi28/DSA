class Solution:
    def func(self, i, j, arr, dp):
        # Base case: when only one matrix is left (no multiplication needed)
        if i == j:
            return 0

        # Return already computed result to avoid recomputation (Memoization)
        if dp[i][j] != -1:
            return dp[i][j]

        # Initialize with +infinity to find the minimum
        mini = float('inf')

        # Partition the problem at every index k from i to j-1
        for k in range(i, j):
            # Cost of multiplying the left subchain (i to k)
            # + cost of multiplying the right subchain (k+1 to j)
            # + cost of multiplying the two resulting matrices
            steps = arr[i - 1] * arr[k] * arr[j] + self.func(i, k, arr, dp) + self.func(k + 1, j, arr, dp)

            # Update the minimum cost
            mini = min(mini, steps)

        # Store the result in dp table before returning
        dp[i][j] = mini
        return dp[i][j]

    def matrixMultiplication(self, arr):
        # Total number of matrices is len(arr) - 1
        n = len(arr)

        # Initialize dp table with -1 for memoization
        dp = [[-1] * n for _ in range(n)]

        # We compute the result from matrix 1 to matrix n-1
        return self.func(1, n - 1, arr, dp)
