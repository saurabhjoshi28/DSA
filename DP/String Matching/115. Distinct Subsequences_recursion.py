class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)

        # Intuition:
        # We need to count the number of distinct subsequences in 's' that are equal to 't'.
        # At every character of s, we have a choice:
        # - If s[i] == t[j], we can either pick it or skip it.
        # - If s[i] != t[j], we can only skip it.
        # So it's like: how many ways can we match t[0...j] in s[0...i]?

        # Recursive helper function
        def func(i, j):
            # Base Case 1:
            # If j < 0: we have matched all of 't' successfully
            return 1 if j < 0 else 0

            # Base Case 2:
            # If i < 0 but t is still left → no way to match
            if i < 0:
                return 0

            # If characters match, we have two choices:
            if s[i] == t[j]:
                # 1. Pick the current character from s → move both i and j back
                # 2. Don't pick the current character → move only i back
                pick = func(i - 1, j - 1)
                not_pick = func(i - 1, j)
                return pick + not_pick
            else:
                # If characters don't match, we can't pick it → just move i back
                return func(i - 1, j)

        # Example:
        # s = "babgbag", t = "bag"
        # We can form "bag" in 5 different ways as a subsequence in s:
        # - b a g
        # - b a g
        # - b a g
        # - b a g
        # - b a g (with different b/a/g each time from s)
        # We are counting all such paths recursively

        return func(n1 - 1, n2 - 1)
