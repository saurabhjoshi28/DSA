class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # Step 1: Precompute palindrome table
        # is_pal[i][j] will be True if s[i...j] is a palindrome
        is_pal = [[False] * n for _ in range(n)]

        # Fill the table using bottom-up approach
        for i in range(n - 1, -1, -1):        # Start from the end
            for j in range(i, n):             # Check substrings from i to end
                # A substring s[i..j] is a palindrome if:
                # 1. s[i] == s[j], and
                # 2. either length <= 2 or the inner substring s[i+1...j-1] is also a palindrome
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        # Step 2: Build dp array
        # dp[i] stores the minimum number of cuts needed for s[i:]
        dp = [0] * (n + 1)  # dp[n] = 0 by default (base case)

        # Fill dp from right to left
        for i in range(n - 1, -1, -1):
            mini = float('inf')
            for j in range(i, n):
                if is_pal[i][j]:
                    # If s[i...j] is a palindrome, make a cut after j
                    cost = 1 + dp[j + 1]
                    mini = min(mini, cost)
            dp[i] = mini

        # Final result is dp[0] - 1 (because we count one extra cut after the last character)
        return dp[0] - 1
