class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s, count = 0, 0  # s: running prefix sum, count: total number of subarrays with sum = k

        prefix_sum = {}  # Stores frequency of each prefix sum encountered

        for i in range(n):
            s += nums[i]  # Update the running prefix sum

            # If the entire subarray from index 0 to i has sum = k
            if s == k:
                count += 1

            # Check if there exists a prefix sum 's - k'
            # If so, it means the subarray ending at index i sums to k
            if (s - k) in prefix_sum:
                count += prefix_sum[s - k]  # Add the number of times (s - k) has occurred

            # Store the current prefix sum in the map
            # If it already exists, increment its frequency
            if s not in prefix_sum:
                prefix_sum[s] = 1
            else:
                prefix_sum[s] += 1

        return count
