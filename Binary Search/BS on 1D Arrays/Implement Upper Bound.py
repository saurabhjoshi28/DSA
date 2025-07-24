class Solution:
    def upperBound(self, arr, target):
        # -------------------------------------------------------------------
        # Upper Bound using Binary Search
        # -------------------------------------------------------------------
        #
        # Problem
        # -------
        # Given a **sorted** array `arr` and a value `target`,
        # return the **smallest index** `i` such that:
        #       arr[i] > target
        #
        # If such index does **not exist**, return `n` (i.e., arr size).
        #
        # Example:
        # --------
        # arr = [1, 3, 3, 5, 7], target = 3
        # → arr[3] = 5 is the first element > 3 → return 3
        #
        # arr = [1, 2, 3], target = 5
        # → no element > 5 → return 3 (size of array)
        #
        # Approach
        # --------
        # We apply binary search to find the **first index** where
        # the element is **strictly greater** than the target.
        #
        # We initialize:
        #   - low = 0 (start of search space)
        #   - high = n - 1 (end of search space)
        #   - upper_bound = n (default answer if not found)
        #
        # At each step:
        #   - if arr[mid] > target:
        #       → it's a **valid candidate**, but there may be an earlier one
        #       → so we update upper_bound = mid, and move high = mid - 1
        #   - else:
        #       → move right: low = mid + 1
        #
        # Time Complexity: O(log N)
        # Space Complexity: O(1)
        # -------------------------------------------------------------------

        n = len(arr)
        low, high = 0, n - 1
        upper_bound = n  # default value if no element > target

        while low <= high:
            mid = (low + high) // 2

            # Candidate found, but try to find earlier one
            if arr[mid] > target:
                upper_bound = mid
                high = mid - 1
            # Search in right half
            else:
                low = mid + 1

        return upper_bound
