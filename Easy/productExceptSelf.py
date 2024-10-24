class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myList = []

        leftList = [1]

        index = 1
        while index < len(nums):
            leftList.append(leftList[index - 1] * nums[index - 1])
            index += 1

        rightList = [1]
        index2 = len(nums) - 2
        while index2 > -1:
            rightList.append(rightList[-1] * nums[index2 + 1])
            index2 -= 1
        rightList.reverse()

        index3 = 0
        while index3 < len(nums):
            myList.append(rightList[index3] * leftList[index3])
            index3 += 1

        return myList
