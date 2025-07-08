class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        🧠 Intuition:
        - We need to ship all packages in `days` days.
        - Each day we can load packages onto the ship (in order, can't split packages).
        - Goal: Find the **minimum ship capacity** needed to do this.

        ✅ Approach:
        - The minimal capacity we could possibly have is `max(weights)` (otherwise the heaviest package wouldn't fit).
        - The maximal capacity we could possibly have is `sum(weights)` (ship all packages in a single day).
        - Our search space is [max(weights), sum(weights)].

        - We can binary search on capacity:
          - For each capacity, simulate: how many days do we need to ship all packages?
          - If it fits in `days` days → try smaller capacity (left half).
          - Else → need larger capacity (right half).
        """

        n = len(weights)
        low, high = max(weights), sum(weights)
        ans = 0

        def func(cap):
            """
            For given ship capacity cap, simulate shipping process.
            Returns True if we can ship in <= days days.
            """
            d = 1  # start with first day
            current_weight = 0
            for i in range(n):
                if current_weight + weights[i] > cap:
                    # current package doesn't fit → need new day
                    d += 1
                    current_weight = 0
                current_weight += weights[i]
            return d <= days

        # ⚡ Binary search for minimal possible capacity
        while low <= high:
            mid = (low + high) // 2
            if func(mid):
                # Possible to ship in given days with capacity mid → try smaller
                ans = mid
                high = mid - 1
            else:
                # Need larger capacity
                low = mid + 1
        return ans

        """
        ⏱ Time Complexity: O(n * log(sum(weights) - max(weights)))
        📦 Space Complexity: O(1)

        🧪 Example:
        weights = [1,2,3,4,5,6,7,8,9,10], days=5
        Search space: [10, 55]
        Try mid=32 → simulate, need 4 days → possible → try smaller capacity.
        Keep narrowing down to find minimal capacity.
        """
