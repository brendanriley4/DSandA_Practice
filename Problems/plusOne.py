from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        i = 0
        while i < len(digits):
            if digits[i] + 1 < 10:
                digits[i] = digits[i] + 1
                break
            digits[i] = 0
            i += 1
        if i == len(digits):
            digits.append(1)
        digits.reverse()
        return digits


if __name__ == '__main__':
    solution = Solution()

    testCase = [1,2,3]
    ans = solution.plusOne(testCase)
    print(f"test case 1: {ans} \n")

    testCase2 = [4,3,2,1]
    ans = solution.plusOne(testCase2)
    print(f"test case 2: {ans} \n")

    testCase3 = [9, 9, 9, 9]
    ans = solution.plusOne(testCase3)
    print(f"test case 2: {ans} \n")