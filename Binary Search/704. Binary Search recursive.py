class Solution:
    # ---------------------------------------------------------------------
    # Binary Search – Recursive Implementation
    # ---------------------------------------------------------------------
    #
    # Problem
    # -------
    # Given a **sorted** array `nums` and an integer `target`,
    # return the index of `target` if it exists, otherwise return `-1`.
    #
    # Why Binary Search?
    # ------------------
    # Because the array is sorted in ascending order, we can repeatedly cut
    # the search space in half, achieving O(log N) time complexity.
    #
    # Function `func`
    # ---------------
    # A recursive helper that searches the sub‑array `nums[low … high]`.
    #
    #   • Base‑case 1: If `low > high`, the search space is empty → return `-1`.
    #   • Base‑case 2: If `nums[mid] == target`, we’ve found the element →
    #     return `mid`.
    #   • Recursive step:
    #       – If `target` is smaller than `nums[mid]`, search the **left half**  
    #         (`low … mid‑1`).
    #       – Otherwise search the **right half** (`mid+1 … high`).
    #
    # Complexity
    # ----------
    # • **Time:** `O(log N)` – each recursive call halves the search space.  
    # • **Space:** `O(log N)` – call‑stack depth in the worst case.
    # ---------------------------------------------------------------------

    def func(self, low, high, target, nums):
        # Base‑case 1: search space exhausted → target not found
        if low > high:
            return -1

        # Midpoint of current search space
        mid = (low + high) // 2

        # Base‑case 2: target found
        if nums[mid] == target:
            return mid

        # Recursive search in the left half
        elif nums[mid] > target:
            return self.func(low, mid - 1, target, nums)

        # Recursive search in the right half
        else:
            return self.func(mid + 1, high, target, nums)

    def search(self, nums: List[int], target: int) -> int:
        """
        Public wrapper that initiates recursive binary search.
        """
        return self.func(0, len(nums) - 1, target, nums)
