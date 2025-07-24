class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        🧠 Intuition:
        - We have to make `m` bouquets, each consisting of `k` adjacent flowers.
        - Each flower blooms on bloomDay[i]. We want to find the **minimum day** so that it's possible to make these bouquets.
        - Since we have a clear monotonic behavior: if it's possible on day `d`, it will also be possible on any day > d.
        - This suggests using **binary search on answer / day** to find the minimal day.

        ✅ Approach:
        - Search space: [min(bloomDay), max(bloomDay)]
        - For each candidate day, check if it's possible to make at least m bouquets.
        - If possible → try smaller day (search left); else → search right.
        """

        n = len(bloomDay)
        first_day = min(bloomDay)
        last_day = max(bloomDay)

        # Quick check: if total flowers needed > available flowers → impossible
        if m * k > n:
            return -1

        def possible(day):
            """
            For given day, check if we can make at least m bouquets.
            Each bouquet needs k consecutive bloomed flowers.
            """
            count = 0  # count consecutive bloomed flowers
            no_of_bouquets = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    # Form bouquets from current streak
                    no_of_bouquets += (count // k)
                    count = 0
            # Last streak (in case array ends with bloomed flowers)
            no_of_bouquets += (count // k)
            return no_of_bouquets >= m

        # 🐌 Brute force: check every day → O(n * range of days)
        # for day in range(first_day, last_day + 1):
        #     if possible(day):
        #         return day
        # return -1

        # ⚡ Optimal → binary search on answer
        low, high = first_day, last_day
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                ans = mid  # found possible day, try to find earlier day
                high = mid - 1
            else:
                low = mid + 1
        return ans

        """
        🧪 Example dry run:
        bloomDay = [1,10,3,10,2], m=3, k=1
        We need 3 flowers; since k=1, just need 3 days with flowers bloomed.
        min=1, max=10 → binary search [1,10]

        ⏱ Time Complexity: O(n * log(max(bloomDay)))
        📦 Space Complexity: O(1)
        """
