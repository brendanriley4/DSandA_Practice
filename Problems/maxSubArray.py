from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # WE CAN DO BETTER!
        max_sum = float('-inf')
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum

        # standard recursive implementation
        # max_sum = [float('-inf')]
        # def recurse(summ, index):
        #     if summ > max_sum[0]:
        #         max_sum[0] = summ
        #     if index >= len(nums):
        #         return
        #     recurse(summ + nums[index], index + 1)
        #     recurse(0, index + 1)
        #
        # recurse(0, 0)
        # return max_sum[0]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxSubArray([1])
    print(ans)