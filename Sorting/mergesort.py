class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 🔁 Merge two sorted subarrays nums[low..mid] and nums[mid+1..high]
        def merge(low, mid, high):
            left = low               # pointer for left half
            right = mid + 1         # pointer for right half
            temp = []               # temporary array to store merged result

            # 🟢 Compare and pick smaller element from both halves
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            # 🔸 Append remaining elements from left half
            while left <= mid:
                temp.append(nums[left])
                left += 1

            # 🔸 Append remaining elements from right half
            while right <= high:
                temp.append(nums[right])
                right += 1

            # 🔄 Copy merged result back to original array
            for i in range(low, high + 1):
                nums[i] = temp[i - low]

        # 🧠 Divide-and-Conquer: recursively split and merge
        def mergesort(low, high):
            if low == high:
                return  # base case: single element is already sorted

            mid = (low + high) // 2

            # 🔽 Sort left half
            mergesort(low, mid)

            # 🔼 Sort right half
            mergesort(mid + 1, high)

            # 🧩 Merge sorted halves
            merge(low, mid, high)

        # ⏯️ Start sorting entire array
        mergesort(0, n - 1)
        return nums
