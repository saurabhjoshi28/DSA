class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        🧠 Intuition:
        We need to find the starting and ending positions of a given `target` in a sorted array.
        Since the array is sorted, we can use binary search to do this efficiently.

        👉 We do two binary searches:
        1️⃣ Find the **first occurrence** (lower bound) of target.
        2️⃣ Find the **first index greater than target** (upper bound).

        The range of target in nums will be:
            [lower_bound, upper_bound - 1]

        ⚠️ Edge Case:
        If target is not present:
        - `lower_bound` may go out of bounds (`n`)
        - or nums[lower_bound] != target
        In that case, we return [-1, -1].
        """

        n = len(nums)
        lower_bound = n  # stores first index >= target
        upper_bound = n  # stores first index > target

        # ✅ First binary search to find upper_bound (smallest number > target)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                upper_bound = mid
                high = mid - 1  # move left
            else:
                low = mid + 1   # move right

        # ✅ Second binary search to find lower_bound (smallest index with nums[mid] >= target)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lower_bound = mid
                high = mid - 1  # move left
            else:
                low = mid + 1   # move right

        # ⚠️ Check if target is actually present
        if not nums or lower_bound == n or nums[lower_bound] != target:
            return [-1, -1]
        else:
            # upper_bound - 1 gives the last occurrence of target
            return [lower_bound, upper_bound - 1]

        """
        ⏱️ Time Complexity: O(log N) for each binary search → overall O(log N)
        📦 Space Complexity: O(1) (we only use variables)
        """
