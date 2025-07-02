class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        🧠 Intuition:
        - The array is sorted but rotated at some pivot.
        - So at any point, either the left half or the right half must be sorted.
        - We check which half is sorted and then see if the target lies in that half.
          - If yes → binary search in that half.
          - If not → binary search in the other half.
        - This way, we still keep O(log N) time.

        📦 Idea:
        - Use standard binary search, but add logic to decide which half is sorted.
        """

        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return mid

            # ✅ Case 1: Left half nums[low..mid] is sorted
            if nums[low] <= nums[mid]:
                # Check if target lies in this sorted left half
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1  # search left
                else:
                    low = mid + 1   # search right half

            # ✅ Case 2: Right half nums[mid..high] is sorted
            else:
                # Check if target lies in this sorted right half
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1   # search right
                else:
                    high = mid - 1  # search left half

        # ❌ Not found
        return -1

        """
        ⏱️ Time Complexity: O(log N) 
        📦 Space Complexity: O(1)

        🧪 Example Dry Run:
        nums = [4,5,6,7,0,1,2], target=0
        - mid=3 (nums[3]=7), left half [4,5,6,7] is sorted
          target=0 not in [4,5,6,7], so search right
        - mid=5 (nums[5]=1), right half [0,1,2] is sorted
          target=0 in [0,1,2], so narrow down
        - mid=4 → nums[4]=0 == target → found
        """
