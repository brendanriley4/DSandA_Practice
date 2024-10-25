class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0] ** 2]
        myList = []
        ptr1 = len(nums) - 2
        ptr2 = len(nums) - 1
        for num in nums:
            if num >= 0:
                ptr2 = nums.index(num)
                if ptr2 != 0:
                    ptr1 = ptr2 - 1
                else:
                    i = 0
                    while i < len(nums):
                        nums[i] = nums[i] ** 2
                        i += 1
                    return nums
                break
        while ptr1 >= 0 or ptr2 < len(nums):
            print(f"ptr1: {ptr1}, ptr2: {ptr2}")
            if ptr1 == -1:
                myList.append(nums[ptr2] ** 2)
                ptr2 += 1
            elif ptr2 == len(nums):
                myList.append(nums[ptr1] ** 2)
                ptr1 -= 1
            elif abs(nums[ptr1]) < abs(nums[ptr2]):
                myList.append(nums[ptr1] ** 2)
                ptr1 -= 1
            else:
                myList.append(nums[ptr2] ** 2)
                ptr2 += 1

        return myList

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [-4, -1, 0, 3, 10],    # Expected output: [0, 1, 9, 16, 100]
        [-7, -3, 2, 3, 11],    # Expected output: [4, 9, 9, 49, 121]
        [1, 2, 3, 4],          # Expected output: [1, 4, 9, 16]
        [-5, -3, -2, -1],      # Expected output: [1, 4, 9, 25]
        [2, 3, 3, 4],          # Expected output: [0, 0, 1, 4]
    ]

    for i, nums in enumerate(test_cases):
        result = solution.sortedSquares(nums)
        print(f"Test Case {i + 1}: Input: {nums}, Output: {result}")