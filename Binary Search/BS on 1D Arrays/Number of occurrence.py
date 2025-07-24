class Solution:
    def countFreq(self, arr, target):
        # ------------------------------------------------------------
        # Problem: Count Frequency of target in a Sorted Array
        # ------------------------------------------------------------
        # Idea: Use Binary Search to find:
        # 1. First Occurrence (Ceil → leftmost index of target)
        # 2. Last Occurrence (Floor → rightmost index of target)
        # Frequency = (floor - ceil + 1)
        # ------------------------------------------------------------
        # Time Complexity: O(log N)
        # Space Complexity: O(1)
        # ------------------------------------------------------------

        n = len(arr)
        floor, ceil = -1, -1  # initialize floor and ceil

        # Step 1: Find Ceil (first occurrence of target)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                ceil = mid         # possible first occurrence
                high = mid - 1     # go left to find earlier occurrence
            else:
                low = mid + 1      # go right

        # Step 2: Find Floor (last occurrence of target)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                floor = mid        # possible last occurrence
                low = mid + 1      # go right to find later occurrence
            else:
                high = mid - 1     # go left

        # Step 3: Return frequency if target exists in array
        if not arr or arr[floor] != target:
            return 0              # target not found
        else:
            return floor - ceil + 1  # count of target's appearances
