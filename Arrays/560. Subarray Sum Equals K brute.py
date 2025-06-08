class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0  # To store the total number of subarrays with sum equal to k

        # Iterate over all possible subarrays
        for i in range(n):
            for j in range(i, n):
                s = 0  # Variable to store sum of current subarray nums[i...j]

                # Compute the sum of subarray nums[i...j]
                for idx in range(i, j + 1):
                    s += nums[idx]

                # If the sum equals k, we increment the count
                if s == k:
                    count += 1

        # Return the total count of valid subarrays
        return count
