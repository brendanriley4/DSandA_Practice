from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, sol = [], []

        def backtrack():
            if sum(sol) == target:
                ans.append(sol[:])
                return
            if sum(sol) > target or len(sol) == len(candidates):
                return
            for num in candidates:
                ans.append(num)
                backtrack()
                ans.pop()

        return ans


if __name__ == '__mai__':
    solution = Solution()

    print(solution.combinationSum([2,3,6,7], 7))