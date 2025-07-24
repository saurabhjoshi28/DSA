class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)  # n piles of bananas

        # Check if Koko can eat all bananas at speed 'k' within 'h' hours
        def possible(k):
            count_hours = 0
            for i in range(n):
                # Ceil division without math.ceil
                count_hours += (piles[i] + k - 1) // k
                if count_hours > h:
                    return False
            return True

        low, high = 1, max(piles)  # min and max possible eating speed
        ans = high  # worst case: eat at max speed

        while low <= high:
            mid = (low + high) // 2  # try mid speed
            if possible(mid):
                ans = mid           # possible, but try smaller speed
                high = mid - 1
            else:
                low = mid + 1       # not possible, need to eat faster

        return ans
