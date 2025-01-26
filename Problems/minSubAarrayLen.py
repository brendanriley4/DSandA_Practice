from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        min_length = float('inf')
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                min_length = min(min_length, r - l + 1)
                summ -= nums[l]
                l += 1
        if min_length == float('inf'): return 0
        return min_length

if __name__ == '__main__':
    solution = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(solution.minSubArrayLen(target, nums))