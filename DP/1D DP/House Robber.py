# 🏠 Problem: House Robber
# Given a list of non-negative integers nums representing the amount of money of each house,
# we cannot rob adjacent houses. Find the maximum amount you can rob.

# ✅ Brute force (recursive): Try robbing or skipping each house.

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        🧠 Intuition:
        - At every index, we have two choices:
            1. Rob this house → cannot rob the next one → move to i-2.
            2. Skip this house → move to i-1.
        - Take the max of these two.
        """
        n = len(nums)
        def func(i):
            if i < 0:
                return 0
            robbing = nums[i] + func(i - 2)
            not_robbing = func(i - 1)
            return max(robbing, not_robbing)
        return func(n - 1)

"""
⏱ Time: O(2^n) (since every call branches into two),
📦 Space: O(n) recursion stack
"""

# ------------------------------------------------------------

# ✅ Memoization: cache subproblems

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        🧠 Same idea as brute force,
        but store already-computed results in dp[i] to avoid recomputation.
        """
        n = len(nums)
        dp = [-1] * n
        def func(i):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            robbing = nums[i] + func(i - 2)
            not_robbing = func(i - 1)
            dp[i] = max(robbing, not_robbing)
            return dp[i]
        return func(n - 1)

"""
⏱ Time: O(n)
📦 Space: O(n) dp + O(n) recursion stack
"""

# ------------------------------------------------------------

# ✅ Tabulation: bottom-up DP

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        🧠 Build the solution iteratively:
        - dp[i] = max money till house i.
        - Either rob i: nums[i-1] + dp[i-2]
        - Or skip i: dp[i-1]
        
        Index shifting: dp[0]=0, dp[1]=nums[0].
        """
        n = len(nums)
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, n + 1):
            robbing = nums[i - 1] + dp[i - 2]
            not_robbing = dp[i - 1]
            dp[i] = max(robbing, not_robbing)
        return dp[n]

"""
⏱ Time: O(n)
📦 Space: O(n)
"""

# ------------------------------------------------------------

# ✅ Space optimized: only keep last two dp values

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        🧠 Since at step i we only need dp[i-1] and dp[i-2],
        we can store them in two variables (prev1 and prev0).
        """
        n = len(nums)
        if n == 0:
            return 0
        prev0 = 0          # dp[i-2]
        prev1 = nums[0]    # dp[i-1]
        for i in range(2, n + 1):
            robbing = nums[i - 1] + prev0
            not_robbing = prev1
            curr = max(robbing, not_robbing)
            prev0 = prev1
            prev1 = curr
        return prev1

"""
⏱ Time: O(n)
📦 Space: O(1)
"""

# ------------------------------------------------------------

"""
✅ Summary of ideas:
- Brute force: explore every choice → exponential.
- Memoization: cache answers → avoid recomputation.
- Tabulation: build answers iteratively from base cases.
- Space optimization: only keep what we need.

💡 All rely on the same core intuition:
At each house, choose:
- Rob → skip next
- Skip → move to next
and take the maximum.
"""
