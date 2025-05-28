class Solution:
    def func(self, i, j, arr):
        """
        Recursive function to find the minimum number of scalar multiplications
        needed to multiply matrices from index i to j.

        Partition DP Idea:
        ------------------
        - We want to solve the problem of multiplying matrices A[i] to A[j].
        - We try all possible positions 'k' to split the problem into two parts:
            1. Multiply matrices from A[i] to A[k]
            2. Multiply matrices from A[k+1] to A[j]
        - We then calculate the cost of combining these two results, which is:
            arr[i-1] * arr[k] * arr[j]
        - The total cost for this partition is:
            cost = cost_left + cost_right + cost_to_multiply_two_parts
        - We do this for every k from i to j-1 and return the **minimum** cost.

        Base Case:
        ----------
        - If i == j, we are left with only one matrix.
        - No multiplication is needed, so return 0.
        """
        if i == j:
            return 0

        mini = float('inf')  # Initialize with max possible

        # Try all partitions k between i and j
        for k in range(i, j):
            # Cost to multiply the two resulting matrices + cost of left and right recursive calls
            steps = (
                arr[i - 1] * arr[k] * arr[j] +  # Cost of multiplying the two parts
                self.func(i, k, arr) +          # Cost of multiplying matrices from i to k
                self.func(k + 1, j, arr)        # Cost of multiplying matrices from k+1 to j
            )

            # Update the minimum cost
            mini = min(mini, steps)

        return mini

    def matrixMultiplication(self, arr):
        """
        Main function that initializes the recursive call.

        Input:
        ------
        - arr: List[int], where arr[i] is the number of rows/columns of matrix Ai

        Output:
        -------
        - Minimum number of scalar multiplications required to multiply the chain
        """
        n = len(arr)  # Total number of elements (matrices are from A1 to A(n-1))
        return self.func(1, n - 1, arr)
