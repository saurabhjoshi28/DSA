class Solution:
    # User function Template for python3

    # Function to find the floor of 'x' in a sorted array
    def findFloor(self, arr, x):
        # -------------------------------------------------------------------
        # FLOOR in a sorted array
        # -------------------------------------------------------------------
        #
        # Definition:
        # The floor of a number 'x' in a sorted array is the
        # greatest element in the array that is **less than or equal to x**.
        #
        # In other words, floor(x) = max(arr[i]) such that arr[i] <= x
        #
        # We need to return the **index** of the floor element.
        # If no such element exists (i.e., all elements > x), return -1.
        #
        # Example:
        # arr = [1, 2, 4, 6, 10], x = 5
        # → floor of 5 is 4 → index = 2
        #
        # arr = [1, 2, 4, 6, 10], x = 10
        # → floor of 10 is 10 → index = 4
        #
        # arr = [1, 2, 4, 6, 10], x = 0
        # → no element <= 0 → return -1
        #
        # -------------------------------------------------------------------
        # Approach (Binary Search):
        # -------------------------------------------------------------------
        # We use binary search to find the **largest index** where
        # arr[mid] <= x
        #
        # 1. Initialize low = 0, high = n - 1, ans = -1
        # 2. While low <= high:
        #    - If arr[mid] <= x:
        #        - It's a valid candidate, but maybe there's a bigger one
        #        - Store mid in ans, and search right half → low = mid + 1
        #    - Else:
        #        - arr[mid] > x → move to left half → high = mid - 1
        #
        # At the end, ans will contain the index of the floor
        # or -1 if not found.
        #
        # -------------------------------------------------------------------
        # Time Complexity: O(log N)
        # Space Complexity: O(1)
        # -------------------------------------------------------------------

        ans = -1
        n = len(arr)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] <= x:
                # Valid candidate → move right to find a larger one
                ans = mid
                low = mid + 1
            else:
                # Current element is too big → try smaller values
                high = mid - 1

        return ans
