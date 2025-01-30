
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        if len(nums) == 1: return True
        last = len(nums) - 1
        move = last - 1
        while move >= 0:
            if nums[move] >= last - move:
                last = move
            move -= 1
            if last == 0:
                return True
        return False






if __name__ == '__main__':
    solution = Solution()

    testCase = [2,3,1,1,4]
    out = solution.canJump(testCase)
    print(out)

    testCase2 = [3,2,1,0,4]
    out = solution.canJump(testCase2)
    print(out)

    testCase3 = [0, 2, 3]
    out = solution.canJump(testCase3)
    print(out)