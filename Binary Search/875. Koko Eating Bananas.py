class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        🧠 Intuition:
        - Koko needs to finish all piles of bananas in h hours.
        - She can choose an integer eating speed k (bananas per hour). 
        - For each pile, time to finish = ceil(pile/k).
        - We need to find the **minimum** k such that total time ≤ h.

        ✅ Brute force:
        - Try every possible k from 1 to max(piles).
        - For each k, calculate total hours needed and check if ≤ h.
        - First k which satisfies is our answer.
        """

        n = len(piles)
        m = max(piles)  # Max possible speed (can't go beyond largest pile)

        def func(speed):
            """
            For given eating speed `speed`, compute total hours needed.
            """
            total = 0
            for i in range(n):
                total += ceil(piles[i] / speed)
            return total

        # Try all speeds from 1 to max pile
        for speed in range(1, m + 1):
            remaining = func(speed)
            if remaining <= h:
                return speed  # Found the minimum valid speed

        """
        ⚡ Note:
        - This brute force approach is correct but inefficient.
        - Optimal solution uses binary search on speed:
          - Search space = [1, max(piles)].
          - At each mid speed, compute total hours and adjust low/high.

        🧪 Dry run example:
        piles=[3,6,7,11], h=8
        Try speed=1 → takes too long.
        Try speed=4 → total hours=8, fits → answer=4

        ⏱ Time Complexity: O(m * n), where m=max(piles)
        📦 Space Complexity: O(1)
        """
# now we will optimise

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        🧠 Intuition:
        - We need to find the **minimum eating speed** k so that Koko can eat all the bananas within h hours.
        - Each hour she can eat up to k bananas.
        - For each pile, the time needed is ceil(pile / k).
        - The lower the speed k, the longer it takes. Higher k finishes faster.
        - Since k is an integer in range [1, max(piles)], and as k increases total hours strictly decrease,
          we can apply **binary search** to find the minimal valid k.

        ✅ Approach:
        - Search space: [1, max(piles)].
        - For each candidate speed (mid), calculate total hours needed:
            - if total hours <= h → k might be too high; look for smaller k (high = mid - 1)
            - else → k is too low; need higher speed (low = mid + 1)
        - Keep track of the best answer so far.
        """

        n = len(piles)
        m = max(piles)

        def func(speed):
            """
            For a given eating speed `speed`, compute total hours needed.
            - Note: we use -(-a//b) instead of math.ceil(a/b) because ceil(a/b) = -(-a//b)
              This avoids importing extra modules and works efficiently.
            """
            total = 0
            for i in range(n):
                total += -(-piles[i]//speed)
            return total

        # Binary search to find minimal k
        low, high = 1, m
        ans = m  # Initialize with max possible speed
        while low <= high:
            mid = (low + high) // 2
            rem = func(mid)
            if rem <= h:
                ans = mid  # Found a valid k, try to minimize
                high = mid - 1
            else:
                low = mid + 1
        return ans

        """
        🧪 Example dry run:
        piles=[3,6,7,11], h=8
        max pile=11 → search space [1,11]
        mid=6 → total hours=4 → ok → ans=6 → search left
        mid=3 → total=8 → ok → ans=3 → search left
        mid=2 → total=11 > 8 → too slow → search right
        mid=4 → total=7 → ok → ans=4 → search left
        Final ans=4

        ⏱ Time Complexity: O(n * log(max(piles)))
        📦 Space Complexity: O(1)
        """
