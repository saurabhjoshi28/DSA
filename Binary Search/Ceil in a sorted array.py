class Solution:
    # Function to find the ceiling of 'x' in a sorted array
    def findCeil(self, arr, x):
        # -------------------------------------------------------------------
        # CEILING in a sorted array
        # -------------------------------------------------------------------
        #
        # Definition:
        # The ceiling of a number 'x' is the **smallest element**
        # in the array which is **greater than or equal to x**.
        #
        # ceiling(x) = min(arr[i]) such that arr[i] >= x
        # We return the **index** of this element.
        #
        # If no such element exists, return -1.
        #
        # -------------------------------------------------------------------
        # Approach (Binary Search):
        # -------------------------------------------------------------------
        # 1. Initialize low = 0, high = n - 1, ans = -1
        # 2. While low <= high:
        #    - If arr[mid] >= x:
        #        - It's a valid candidate → store in ans
        #        - But maybe there's a smaller one on the left
        #        → high = mid - 1
        #    - Else:
        #        - arr[mid] < x → try larger values → low = mid + 1
        #
        # Return ans.
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

            if arr[mid] >= x:
                # Valid ceiling candidate → try to find smaller on left
                ans = mid
                high = mid - 1
            else:
                # Current is too small → move right
                low = mid + 1

        return ans
