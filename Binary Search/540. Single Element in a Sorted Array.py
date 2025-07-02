class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        🧠 Intuition:
        - The array is sorted and every element appears exactly twice, except for one single element.
        - To find this unique element in O(log N), we use binary search.
        - We observe a **pattern**:
            - On the left of the single element: elements appear as pairs in indices (even, odd)
              e.g., nums = [3, 3, 7, 7, 10, ...] → pairs: (0,1), (2,3)
            - On the right of the single element: pairs start at odd index → (odd, even)
              e.g., [..., 11, 11, 12, 12] → pairs: (5,6), (7,8)

        By checking the pattern at mid, we can decide which half to discard:
            - If mid is even and nums[mid] == nums[mid+1]: single element is on the right.
            - If mid is even and nums[mid] == nums[mid-1]: single element is on the left.
            - Vice versa for odd mid.

        """

        n = len(nums)

        # 🛡️ Handle edge cases when unique element is at boundary
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        # Binary Search starts
        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2

            # ✅ Check if nums[mid] is the unique single element
            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # 🧐 Check which half to search based on pair pattern

            # Case: nums[mid] == nums[mid - 1]
            if nums[mid] == nums[mid - 1]:
                if mid % 2 == 0:
                    # mid is even, so pair starts at odd → we're in right half
                    high = mid - 1
                else:
                    # mid is odd, pair is normal → unique is in right half
                    low = mid + 1

            # Case: nums[mid] == nums[mid + 1]
            elif nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    # mid is even, pair is normal → unique is in right half
                    low = mid + 1
                else:
                    # mid is odd, pair starts at even → we're in left half
                    high = mid - 1

        # Default return (should not reach here as problem guarantees unique element)
        return -1

        """
        🧪 Dry run example:
        nums = [3,3,7,7,10,11,11,12,12,14,14]
        mid=4, nums[4]=10 → nums[3]=7 !=10 and 10!=nums[5]=11 → found!
        
        ✅ Time Complexity: O(log N)
        📦 Space Complexity: O(1)
        """
