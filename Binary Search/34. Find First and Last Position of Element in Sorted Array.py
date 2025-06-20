class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # ------------------------------------------------------------
        # Problem: Find First and Last Occurrence of Target in Sorted Array
        # ------------------------------------------------------------
        # Idea: Use Binary Search twice
        # 1. First to find FLOOR → rightmost index where nums[i] <= target
        # 2. Second to find CEIL → leftmost index where nums[i] >= target
        # ------------------------------------------------------------
        # Time Complexity: O(log N) for each binary search → total: O(log N)
        # Space Complexity: O(1)
        # ------------------------------------------------------------

        floor = -1  # Will store the rightmost occurrence of target
        ceil = -1   # Will store the leftmost occurrence of target

        # Step 1: Binary Search for FLOOR (last occurrence of target)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                floor = mid       # possible last occurrence
                low = mid + 1     # move right to check for later occurrence
            else:
                high = mid - 1    # move left

        # Step 2: Binary Search for CEIL (first occurrence of target)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ceil = mid        # possible first occurrence
                high = mid - 1    # move left to check for earlier occurrence
            else:
                low = mid + 1     # move right

        # Step 3: Validate that target exists at both indices
        if not nums or nums[floor] != target:
            return [-1, -1]
        else:
            return [ceil, floor]
