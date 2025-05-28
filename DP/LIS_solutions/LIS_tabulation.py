class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i][prev + 1] will store the length of LIS starting from index i
        # with the previous picked element being at index prev.
        # We use prev + 1 to handle -1 (i.e., no element picked yet).
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Iterate from the last index to the first
        for i in range(n - 1, -1, -1):

            # prev ranges from i-1 to -1 (we shift -1 to 0 in dp table)
            for prev in range(i - 1, -2, -1):

                pick = float('-inf')

                # Option 1: pick the current element if it's greater than the prev one
                if prev == -1 or nums[prev] < nums[i]:
                    pick = 1 + dp[i + 1][i + 1]  # i becomes the new prev

                # Option 2: don't pick the current element
                not_pick = dp[i + 1][prev + 1]  # shift prev by 1 for indexing

                # Take the best of the two choices
                dp[i][prev + 1] = max(pick, not_pick)

        # dp[0][0] means starting from index 0 with prev = -1 (no previous element)
        return dp[0][-1+1]