from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return False
        myQueue = deque()
        openList = ['{', '(', '['] # could have also used dictionary (oh well)
        closeList = ['}', ')', ']']
        for char in s:
            if char not in openList and char not in closeList:
                return False
            if char in openList:
                myQueue.append(char)
            else:
                if len(myQueue) < 1:
                    return False
                if openList.index(myQueue.pop()) != closeList.index(char):
                    return False
        if len(myQueue) != 0:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()

    testCase = "[]{}()"
    ans = solution.isValid(testCase)
    print(f"test case 1: {ans}, \n")

    testCase2 = "{[]()}"
    ans = solution.isValid(testCase2)
    print(f"test case 1: {ans}, \n")

    testCase3 = "(("
    ans = solution.isValid(testCase3)
    print(f"test case 3: {ans} \n")