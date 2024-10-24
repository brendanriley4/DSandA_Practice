class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # do not modify list while iterating over it!

        # since ascending order, we can use two pointers and only have to compare to the item before the one we evaluate

        ptr2 = 1

        for ptr1 in range(1, len(nums)):
            if nums[ptr1] != nums[ptr1-1]:
                nums[ptr2] = nums[ptr1]
                ptr2 += 1

        return ptr2