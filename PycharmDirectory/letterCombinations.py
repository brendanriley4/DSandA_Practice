from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Time complexity: (terrible) O(4^n)
        # Space complexity: O(n)

        if digits == '':
            return []

        possible = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans, sol = [], []
        n = len(digits)

        def backtrack(i=0):
            if i == n:
                ans.append(''.join(sol))
                return

            for letter in possible[digits[i]]:
                sol.append(letter)
                backtrack(i + 1)
                sol.pop()

            return

        backtrack(0)
        return ans