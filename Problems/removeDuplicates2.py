class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ptr1, ptr2, = 2, 2
        while ptr1 < len(nums):
            if nums[ptr1] != nums[ptr2 - 2]:
                nums[ptr2] = nums[ptr1]
                ptr2 += 1
            ptr1 += 1
        return ptr2
