class Solution:
    def mySqrt(self, x: int) -> int:
        """
        🧠 Intuition:
        - We need to find the square root of x, but return only the integer part (i.e., floor of sqrt(x)).
        - Since multiplication grows rapidly, binary search can efficiently find the largest integer whose square ≤ x.

        ⚡ Approach:
        - Use binary search between 1 and x.
        - At each step, compute mid = (low+high)//2.
        - If mid*mid ≤ x → this could be our answer, but maybe there's a bigger number whose square is still ≤ x.
          So, update ans = mid and move low = mid+1.
        - Else, mid*mid > x → mid is too big, so move high = mid-1.

        ✅ In the end, ans will be the floor of sqrt(x).
        """

        low, high = 1, x
        ans = 0  # Initialize answer to 0 (covers edge case x=0)

        while low <= high:
            mid = (low + high) // 2
            # Check if mid*mid is less than or equal to x
            if mid * mid <= x:
                ans = mid  # store as potential answer
                low = mid + 1  # try to find a bigger mid
            else:
                high = mid - 1  # mid too big, move left

        return ans

        """
        🧪 Dry run example: x=10
        low=1, high=10 → mid=5, 25>10 → high=4
        mid=2, 4≤10 → ans=2, low=3
        mid=3, 9≤10 → ans=3, low=4
        mid=4, 16>10 → high=2
        low>high → return ans=3

        ✅ Time Complexity: O(log x)
        📦 Space Complexity: O(1)
        """
