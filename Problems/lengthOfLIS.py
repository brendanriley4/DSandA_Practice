from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Bottom up dp approach is best!!!

        if not nums:
            return 0

        i, j = 0, 0
        dp = [1] * len(nums)
        while i < len(nums):
            j = 0
            while j < i:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                j += 1
            i += 1
        return max(dp)

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))