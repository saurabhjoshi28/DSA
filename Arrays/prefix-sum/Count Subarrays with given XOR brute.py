class Solution:
    def subarrayXor(self, arr, k):
        # Get the length of the array
        n = len(arr)

        # Initialize a variable to count valid subarrays
        count = 0

        # Outer loop to fix the starting index of subarray
        for i in range(n):
            # Inner loop to fix the ending index of subarray
            for j in range(i, n):
                xor = 0  # To store the XOR of the current subarray

                # Third loop to calculate XOR from index i to j
                for idx in range(i, j + 1):
                    xor = xor ^ arr[idx]  # Compute XOR

                # If XOR of the current subarray is equal to k, increment count
                if xor == k:
                    count += 1

        return count  # Return total count of subarrays with XOR == k
