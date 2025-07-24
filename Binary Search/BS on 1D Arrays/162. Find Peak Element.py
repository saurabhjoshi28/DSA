class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        🧠 Intuition:
        - We are given an array and need to find any "peak element".
          A peak element is defined as nums[i] such that:
            nums[i-1] < nums[i] > nums[i+1]
        - The array can have multiple peaks; we can return any.
        - Since brute force is O(N), we look for O(log N) using binary search.

        ⚡ Observation / Pattern:
        - If nums[mid] < nums[mid+1]: we are on an ascending slope → there must be at least
          one peak on the right (by problem guarantee).
        - If nums[mid] > nums[mid+1]: we are on a descending slope → there must be a peak on the left (could be mid itself).

        So, by checking the slope, we can discard half of the search space at each step.
        """

        n = len(nums)

        # 🛡️ Edge cases: if single element or peak at boundaries
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        # Binary search in the range [1, n-2]
        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2

            # ✅ Check if mid itself is a peak
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            # 🧐 Check the slope to decide the search space
            if nums[mid - 1] < nums[mid]:
                # Ascending slope → go right
                low = mid + 1
            elif nums[mid] > nums[mid + 1]:
                # Descending slope → go left
                high = mid - 1
            else:
                # nums[mid - 1] > nums[mid] < nums[mid + 1]:
                # We are in a valley → arbitrarily choose to go right
                low = mid + 1

        # Note: by problem guarantee, we will always find a peak.
        # So this return won't be reached; added to avoid lint errors.
        return -1

        """
        🧪 Dry run example:
        nums = [1,2,1,3,5,6,4]
        mid=3 → nums[2]=1 < nums[3]=3 < nums[4]=5 → ascending → go right
        mid=5 → nums[4]=5 < nums[5]=6 > nums[6]=4 → found peak at index 5

        ✅ Time Complexity: O(log N)
        📦 Space Complexity: O(1)
        """
