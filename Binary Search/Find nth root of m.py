class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
        # nth root of m 
        low, high = 1, m
        while low <= high:
            mid = (low + high) // 2
            x = 1
            for i in range(n):
                x *= mid
            if x == m:
                return mid
            if x < m:
               low = mid + 1
            else:
                high = mid - 1
        return -1