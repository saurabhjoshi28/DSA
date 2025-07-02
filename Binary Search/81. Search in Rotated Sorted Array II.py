class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        🧠 Intuition:
        - The array is sorted but rotated, **and may have duplicates**.
        - In standard rotated binary search, we decide which half is sorted.
        - But when there are duplicates, nums[low] == nums[mid] == nums[high],
          we can’t decide — so we shrink the search space from both ends.
        - The rest of the logic is similar to rotated binary search:
          - find sorted half → check if target lies there → adjust low/high.
        """

        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            # ⚠️ Special Case: duplicates at boundaries: can't tell which half is sorted
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # ✅ Case 1: Left half nums[low..mid] is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1  # target in left half
                else:
                    low = mid + 1   # target in right half

            # ✅ Case 2: Right half nums[mid..high] is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1   # target in right half
                else:
                    high = mid - 1  # target in left half

        # ❌ Not found
        return False

        """
        🧪 Example Dry Run:
        nums = [2,5,6,0,0,1,2], target=0
        - mid=3 nums[3]=0 → found

        nums = [1,0,1,1,1], target=0
        - mid=2 nums[2]=1, nums[low]=1==nums[mid]==nums[high]=1 → can't decide
        - shrink → low=1, high=3
        - mid=2 again → now left half is sorted → target in left → adjust

        ⏱️ Time Complexity: 
        - Worst: O(N) when there are many duplicates (because of shrinking).
        - Best/Average: O(log N) when duplicates are few.
        📦 Space Complexity: O(1)
        """
