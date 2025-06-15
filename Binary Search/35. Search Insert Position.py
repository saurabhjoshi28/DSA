class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # -------------------------------------------------------------------
        # Search Insert Position using Binary Search
        # -------------------------------------------------------------------
        #
        # Problem:
        # --------
        # Given a sorted list `nums` and a value `target`,
        # return the index if the target is found.
        # If not, return the index where it would be if it were inserted
        # in order (i.e., without breaking the sorting).
        #
        # Example:
        # nums = [1, 3, 5, 6]
        # target = 5 → return 2  (target exists)
        # target = 2 → return 1  (should be inserted at index 1)
        # target = 7 → return 4  (should be inserted at the end)
        #
        # This is exactly the same as finding the **lower bound**
        # i.e., the first index `i` such that nums[i] >= target
        #
        # Approach:
        # ---------
        # We apply binary search with:
        #   - lo = 0
        #   - hi = n - 1
        #   - lower_bound initialized to n (default insertion point)
        #
        # At each step:
        #   - If nums[mid] == target → return mid
        #   - If nums[mid] > target → candidate position → update lower_bound = mid, search left half
        #   - If nums[mid] < target → move right (lo = mid + 1)
        #
        # If not found, we return lower_bound which gives the correct insert position.
        #
        # Time Complexity: O(log N)
        # Space Complexity: O(1)
        #
        # -------------------------------------------------------------------
        # Note:
        # -----
        # Python provides `bisect_left(nums, target)` from the `bisect` module
        # which does the exact same thing — returns the index to insert `target`
        # while maintaining the sorted order.
        #
        # Example:
        # --------
        # from bisect import bisect_left
        # i = bisect_left(nums, target)
        # -------------------------------------------------------------------

        n = len(nums)
        lo, hi = 0, n - 1
        lower_bound = n  # Default insertion point (at end)

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid  # Found the target
            elif nums[mid] > target:
                lower_bound = mid  # Possible insert position
                hi = mid - 1  # Try left half
            else:
                lo = mid + 1  # Search right half

        return lower_bound  # Not found → insert position
