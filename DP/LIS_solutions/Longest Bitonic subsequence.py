from typing import List

class Solution:
    def lis(self, n, nums, dp1):
        """
        Computes the Longest Increasing Subsequence (LIS) ending at every index.
        dp1[i] stores the length of LIS ending at index i.
        """
        for i in range(n):
            for prev in range(i):
                if nums[prev] < nums[i]:
                    dp1[i] = max(dp1[i], 1 + dp1[prev])

    def lds(self, n, nums, dp2):
        """
        Computes the Longest Decreasing Subsequence (LDS) starting at every index.
        dp2[i] stores the length of LDS starting from index i.
        Similar to LIS but in reverse direction.
        """
        for i in range(n - 1, -1, -1):
            for prev in range(n - 1, i, -1):
                if nums[prev] < nums[i]:
                    dp2[i] = max(dp2[i], 1 + dp2[prev])

    def LongestBitonicSequence(self, n: int, nums: List[int]) -> int:
        """
        Returns the length of the Longest Bitonic Subsequence (LBS) in the array.
        
        Concept:
        --------
        A Bitonic sequence is a sequence that first increases then decreases.
        This is built using two LIS-like passes:
        - One forward LIS (`dp1`): computes the increasing part ending at index i.
        - One backward LIS (`dp2`): computes the decreasing part starting from index i.
        
        Final LBS at index i = dp1[i] + dp2[i] - 1
        (we subtract 1 to avoid counting the peak element twice).
        """
        # Initialize LIS and LDS arrays
        dp1, dp2 = [1] * n, [1] * n

        # Step 1: Compute LIS from left to right
        self.lis(n, nums, dp1)

        # Step 2: Compute LDS from right to left
        self.lds(n, nums, dp2)

        # Step 3: Find the maximum length of bitonic sequence
        max_bi = 0
        for i in range(n):
            # We want at least one increasing and one decreasing part
            if dp1[i] > 1 and dp2[i] > 1:
                max_bi = max(max_bi, dp1[i] + dp2[i] - 1)

        return max_bi
