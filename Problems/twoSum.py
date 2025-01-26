class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        myDict = {nums[0]: 0}

        for i in range(1, len(nums)):
            if target - nums[i] in myDict:
                return [i, myDict[target - nums[i]]]
            myDict[nums[i]] = i
        return []