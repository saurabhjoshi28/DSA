class Solution:
    def findKRotation(self, arr):
        """
        🧠 Intuition:
        - The array is originally sorted in ascending order but rotated 'k' times.
        - The number of rotations 'k' is the index of the minimum element.
        - We can find this index using binary search:
            ▸ If arr[low] <= arr[mid]: left part is sorted, so the minimum might be arr[low].
              - If arr[low] < current mini, update mini and its index(ans).
              - Move to right half (low = mid + 1) to keep searching.
            ▸ Else, right part must include pivot, so check arr[mid]:
              - If arr[mid] < current mini, update mini and ans.
              - Move to left half (high = mid - 1).
        """

        n = len(arr)
        mini = float('inf')  # to track minimum element
        ans = 0              # index of minimum element, i.e., number of rotations
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            # ✅ Case 1: Left part arr[low..mid] is sorted
            if arr[low] <= arr[mid]:
                if arr[low] < mini:
                    mini = arr[low]
                    ans = low
                low = mid + 1  # search in right half

            # ✅ Case 2: Right part arr[mid..high] must have pivot
            else:
                if arr[mid] < mini:
                    mini = arr[mid]
                    ans = mid
                high = mid - 1  # search in left half

        return ans

        """
        🧪 Example Dry Run:
        arr = [4,5,6,7,0,1,2]
        mid=3 arr[3]=7, arr[0]=4 → left sorted → mini=4, ans=0 → low=4
        mid=5 arr[5]=1, arr[4]=0 → left not sorted → mini=1, ans=5 → high=4
        mid=4 arr[4]=0 < mini → mini=0, ans=4 → high=3
        Done → ans=4 → array was rotated 4 times

        ⏱️ Time Complexity: O(log N)
        📦 Space Complexity: O(1)
        """
