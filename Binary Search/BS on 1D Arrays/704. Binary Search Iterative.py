class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search Algorithm (Iterative)

        Problem:
        Given a sorted array 'nums' and a target value, return the index of the target if it exists.
        If the target does not exist, return -1.

        Intuition:
        Since the array is sorted in ascending order, we can apply Binary Search which reduces
        the search space by half in every step.

        Approach:
        - Use two pointers: 'low' and 'high' to represent the current search boundaries.
        - Compute the mid index in each iteration using: mid = (low + high) // 2
        - Compare nums[mid] with target:
            - If equal, return mid (target found).
            - If target < nums[mid], move the 'high' pointer left to mid - 1.
            - If target > nums[mid], move the 'low' pointer right to mid + 1.
        - Repeat until low > high. If we exit the loop, the target is not present.
        """

        n = len(nums)
        low, high = 0, n - 1  # Initial search space is the entire array

        while low <= high:
            mid = (low + high) // 2  # Middle index

            if nums[mid] == target:
                return mid  # Target found

            elif nums[mid] > target:
                high = mid - 1  # Discard the right half

            else:
                low = mid + 1  # Discard the left half

        return -1  # Target not found

        """
        Time Complexity: O(log N)
        --------------------------------
        In each step of the loop, the search space is halved:
        e.g., N → N/2 → N/4 → ... → 1
        This can happen at most log₂(N) times.
        So the time complexity is O(log N), where N = number of elements in the array.

        Space Complexity: O(1)
        --------------------------------
        We are using only a constant amount of space (pointers and a few variables),
        so space complexity is constant.
        """
