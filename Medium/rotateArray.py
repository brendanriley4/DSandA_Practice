class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numsBack = nums[-k:]
        nums[:] = nums[:-k]
        nums[:] = numsBack + nums


if __name__ == '__main__':
    solution = Solution()

    testCase, k = [1,2,3,4,5,6,7], 3
    solution.rotate(testCase, k)
    print(f"test case 1: {testCase}")

    testCase2, k2 = [-1,-100,3,99], 2
    solution.rotate(testCase2, k2)
    print(f"test case 2: {testCase2}")

    # testCase3 = " "
    # ans = solution.rotate(testCase3)
    # print(f"test case 3: {ans}, Expected = True\n")