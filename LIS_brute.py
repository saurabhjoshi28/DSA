class Solution:
    def func(self, i, prev, nums):
        n = len(nums)

        # Base case: if we've reached the end of the array
        if i == n:
            return 0

        pick = float('-inf')

        # If we can pick the current element to be part of the increasing subsequence
        if prev == -1 or nums[prev] < nums[i]:
            pick = 1 + self.func(i+1, i, nums)

        # Explore the option of not picking the current element
        notpick = 0 + self.func(i+1, prev, nums)

        # Return the maximum length from picking or not picking the current element
        return max(pick, notpick)

        
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Brute force approach:
        - Generate all possible subsequences using recursion.
        - For each subsequence, check if it's strictly increasing.
        - Keep track of the maximum length of such subsequences.

        The function `func(i, prev, nums)` returns the length of the Longest Increasing Subsequence (LIS)
        starting at index `i` with the last picked element at index `prev`.
        """
        return self.func(0, -1, nums) # this function represents LIS