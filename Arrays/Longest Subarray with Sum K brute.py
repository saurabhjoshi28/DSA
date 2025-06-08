class Solution:
    def longestSubarray(self, arr, k):  
        # Get the size of the array
        n = len(arr)

        # Variable to store the length of the longest subarray with sum k
        max_l = 0

        # Outer loop to fix the starting index 'i' of the subarray
        for i in range(n):

            # Inner loop to fix the ending index 'j' of the subarray
            for j in range(i, n):

                # Initialize sum of the current subarray
                s = 0

                # Loop to calculate the sum of elements from index i to j
                for idx in range(i, j + 1):
                    s += arr[idx]

                # If the subarray sum equals k, update max_l if this subarray is longer
                if s == k:
                    l = (j + 1) - i  # Length of subarray = end - start + 1
                    max_l = max(max_l, l)

        # Return the maximum length found
        return max_l
