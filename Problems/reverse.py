
class Solution:
    def reverse(self, x: int) -> int:
        if not (-2**31 <= x <= 2**31 - 1): return 0
        if x < 0: neg = True
        else: neg = False
        x = abs(x)
        numTemp = []
        newNum, count, i = 0, 0, 0
        while x != 0:
            numTemp.append(x % 10)
            x = x // 10
            count += 1
        while count > 0:
            if numTemp[i] != 0:
                newNum += numTemp[i] * (10 ** (count - 1))
                if (newNum > 2**31 - 1): return 0
            count -= 1
            i += 1
        if neg: newNum *= -1
        if (newNum < -2**31): return 0
        return newNum


if __name__ == '__main__':
    solution = Solution()

    testCase = 123
    ans = solution.reverse(testCase)
    print(f"test case 1: {ans} \n")

    testCase2 = -123
    ans = solution.reverse(testCase2)
    print(f"test case 2: {ans} \n")

    testCase3 = 120
    ans = solution.reverse(testCase3)
    print(f"test case 2: {ans} \n")