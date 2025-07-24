class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        low, high = 1, max(nums)
        ans = 0
        def func(d):
            s = 0
            for i in range(n):
                s += (-(-nums[i]//d))
            return s <= threshold
                 
        while low <= high:
            mid = (low + high) // 2
            if func(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans