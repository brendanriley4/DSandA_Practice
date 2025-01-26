from collections import deque

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) ==  0:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])

        queue = deque()
        valid = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in valid:
                queue.append(token)
            else:
                op1 = queue.pop()
                op2 = queue.pop()
                if token == '+':
                    ans = op2 + op1
                elif token == '-':
                    ans = op2 - op1
                elif token == "*":
                    ans = op2 * op1
                else:
                    ans = int(op2 / op1)
                queue.append(ans)
        return ans

if __name__ == '__main__':
    solution = Solution()

    testCase = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # "123+-"
    ans = solution.evalRPN(testCase)
    print(f"test case 1: Expected = 22, Actual = {ans}")

    testCase2 = ["3","11","+","5","-"]
    ans = solution.evalRPN(testCase2)
    print(f"test case 1: Expected = 9, Actual = {ans}")

    testCase3 = ["3","11","5","+","-"]
    ans = solution.evalRPN(testCase3)
    print(f"test case 3: Expected = -13, Actual = {ans}")


