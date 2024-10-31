class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []

        ans = []
        nums.sort()
        i = 0

        while i < len(nums) - 2:
            target = -nums[i]
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                curr = nums[lo] + nums[hi]
                if curr == target and [nums[i],nums[lo],nums[hi]] not in ans:
                    ans.append([nums[i],nums[lo],nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif curr < target:
                    lo += 1
                else:
                    hi -= 1

            i += 1
        return ans


if __name__ == '__main__':
    solution = Solution()

    testCase = [-1,0,1,2,-1,-4]
    ans = solution.threeSum(testCase)
    print(f"test case 1: {ans}, Expected = [[-1,-1,2],[-1,0,1]\n")

    testCase2 = [0,0,0]
    ans = solution.threeSum(testCase2)
    print(f"test case 2: {ans}, Expected: [0, 0, 0]\n")

    testCase3 = [3,0,-2,-1,1,2]
    ans = solution.threeSum(testCase3)
    print(f"test case 3: {ans}, Expected = [[-2,-1,3],[-2,0,2],[-1,0,1]]\n")