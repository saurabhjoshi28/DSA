class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        🧠 Intuition:
        - The array is originally sorted in ascending order but then rotated.
        - The smallest element will be the rotation pivot.
        - Since the array is sorted in parts, we can use binary search:
          - If nums[low] <= nums[mid], it means the left part nums[low..mid] is sorted.
            → The minimum can only be nums[low] or in the right half, so check nums[low] and move to right.
          - Else, right part nums[mid..high] must be sorted around pivot,
            → The minimum could be nums[mid] or in the left half, so check nums[mid] and move to left.
        """

        n = len(nums)
        low, high = 0, n - 1
        ans = float('inf')  # initialize with large value

        while low <= high:
            mid = (low + high) // 2

            # ✅ Case 1: Left half nums[low..mid] is sorted
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])  # leftmost could be minimum
                low = mid + 1  # search in right half

            # ✅ Case 2: Right half nums[mid..high] is sorted around pivot
            else:
                ans = min(ans, nums[mid])  # mid could be minimum
                high = mid - 1  # search in left half

        return ans

        """
        🧪 Example Dry Run:
        nums = [4,5,6,7,0,1,2]
        - mid=3 nums[3]=7, nums[0]=4 → left half sorted → ans=min(∞,4)=4
          low=4
        - mid=5 nums[5]=1, nums[4]=0 → left half not sorted → ans=min(4,1)=1
          high=4
        - mid=4 nums[4]=0 → left half sorted → ans=min(1,0)=0
          low=5
        Done → answer=0

        ⏱️ Time Complexity: O(log N)
        📦 Space Complexity: O(1)
        """
