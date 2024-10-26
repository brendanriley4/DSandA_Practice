class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            print(f"left = {left}, right = {right}, mid = {mid}")
            if left == right:
                return False
            if mid * mid == num:
                return True
            if mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1

if __name__ == '__main__':
    testCase = 20
    solution = Solution()
    ans = solution.isPerfectSquare(testCase)
    print(f"My Output = {ans}")