class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)

        # 🔍 Intuition:
        # We are trying to match the string `s` with the pattern `p`.
        # The pattern `p` may include:
        # - '?' which matches exactly one character
        # - '*' which matches zero or more of any characters (including empty)

        # We solve this using recursion starting from the last characters of both strings.
        # Let `func(i, j)` represent whether s[0..i] matches p[0..j].

        def func(i, j):
            # ✅ Base Case 1: Both pattern and string are exhausted
            if j < 0 and i < 0:
                return True

            # ❌ Base Case 2: Pattern is exhausted but string still has characters
            if j < 0 and i >= 0:
                return False

            # ✅ Base Case 3: String is exhausted but pattern may contain remaining '*'
            if j >= 0 and i < 0:
                # Remaining pattern must be all '*' to match an empty string
                for c in range(j + 1):
                    if p[c] != '*':
                        return False
                return True

            # 🔁 Case 1: Characters match OR pattern has '?'
            if s[i] == p[j] or p[j] == '?':
                return func(i - 1, j - 1)

            # ✨ Case 2: Pattern has '*'
            # Two choices:
            # a) '*' matches empty sequence → move pattern pointer
            matches_empty = func(i, j - 1)
            # b) '*' matches current character → move string pointer
            matches_a_character = func(i - 1, j)
            return matches_empty or matches_a_character

            # ❌ Case 3: No match
            return False

        return func(n1 - 1, n2 - 1)
