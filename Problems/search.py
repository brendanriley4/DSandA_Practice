import math

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        right = len(nums) - 1
        left = 0

        while left <= right:
            index = (left + right) // 2
            if nums[index] == target:
                return index
            if nums[index] > target:
                # set upper and lower bound
                right = index - 1
            else:
                # set upper and lower bound
                left = index + 1

        return -1