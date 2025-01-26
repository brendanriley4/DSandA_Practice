from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top Down DP (Memoization)
        # Time: O(m*n)
        # Space: O(m*n)

        m , n = len(text1), len(text2)
        @cache
        def longest(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + longest(i+1, j+1)
            return max(longest(i+1, j), longest(i, j+1))

        return longest(0, 0)