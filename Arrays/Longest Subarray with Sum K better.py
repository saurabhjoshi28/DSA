class Solution:
    def longestSubarray(self, arr, k):  
        # Get the length of the array
        n = len(arr)

        # Variable to store the length of the longest subarray with sum k
        max_l = 0

        # Outer loop to fix the starting index 'i' of the subarray
        for i in range(n):
            s = 0  # Initialize sum for the current starting index

            # Inner loop to expand the subarray from i to j
            for j in range(i, n):
                s += arr[j]  # Keep adding elements to the current sum

                # If the subarray sum becomes equal to k
                if s == k:
                    l = (j + 1) - i  # Calculate the current subarray length
                    max_l = max(max_l, l)  # Update max length if this is longer

        # Return the length of the longest valid subarray
        return max_l
