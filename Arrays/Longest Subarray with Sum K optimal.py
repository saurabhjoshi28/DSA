class Solution:
    def longestSubarray(self, arr, k):  
        # Prefix Sum approach:
        # The idea is to use a running sum (prefix sum) and a hashmap to store
        # the first occurrence of each prefix sum value.
        #
        # Prefix sum at index 'i' is the sum of all elements from index 0 to i.
        # So, if prefix_sum[i] - prefix_sum[j] == k, then the subarray (j+1 to i)
        # has a sum of k. We use this observation to find subarrays quickly.

        n = len(arr)
        s, l = 0, 0  # s is running prefix sum, l is max length of subarray with sum = k
        prefix_sum = {}  # stores first occurrence index of each prefix sum value

        for i in range(n):
            s += arr[i]  # update prefix sum with current element

            # Case 1: If prefix sum itself becomes k, then subarray (0 to i) is valid
            if s == k:
                l = max(l, i + 1)

            # Case 2: If there exists a prefix sum such that s - prev = k,
            # then subarray between that previous index +1 to current index has sum = k
            if (s - k) in prefix_sum:
                pre_l = i - prefix_sum[s - k]  # length of this subarray
                l = max(l, pre_l)

            # Case 3: Store the first occurrence of each prefix sum
            # Only first occurrence matters because we want the longest subarray
            # Edge case: If the array contains 0s, the same prefix sum can appear multiple times.
            # So we store only the earliest index to maximize subarray length.
            if s not in prefix_sum:
                prefix_sum[s] = i

        return l
