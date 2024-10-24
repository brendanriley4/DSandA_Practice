class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        valuesSeen = set()
        i = 0

        while i < len(nums):
            if nums[i] in valuesSeen:
                return True
            valuesSeen.add(nums[i])
            i += 1
        return False