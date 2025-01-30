from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = [float('-inf')]
        def subarray(curr_sum, index):
            if index == len(nums):
                return
            max_value[0] = max(curr_sum, max_value[0])
            curr_sum += nums[index]
            subarray(curr_sum, index + 1)
            subarray(0, index + 1)
        subarray(0,0)
        return max_value[0]