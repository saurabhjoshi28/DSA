class Solution:
    def subarrayXor(self, arr, k):
        n = len(arr)
        count = 0         # Initialize the count of subarrays with XOR equal to k
        xor = 0           # This will store the XOR of the subarray from index 0 to i
        prefix_sum = {}   # Hash map to store frequency of prefix XORs

        for i in range(n):
            # Update the prefix XOR up to the current index
            xor = xor ^ arr[i]

            # If prefix XOR is equal to k, we found a subarray from 0 to i
            if xor == k:
                count += 1

            # If (xor ^ k) exists in the map, it means there's a prefix ending before i
            # such that XOR of subarray between that prefix and current i is k
            if (xor ^ k) in prefix_sum:
                count += prefix_sum[xor ^ k]

            # Store or update the frequency of the current prefix XOR
            if xor not in prefix_sum:
                prefix_sum[xor] = 1
            else:
                prefix_sum[xor] += 1

        return count  # Return total number of subarrays with XOR equal to k
