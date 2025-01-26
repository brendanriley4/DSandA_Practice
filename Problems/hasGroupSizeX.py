from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        myDict = Counter(deck)
        myGcd = 0
        for num in myDict.values():
            myGcd = math.gcd(myGcd, num)
        return myGcd > 1

if __name__ == '__main__':
    solution = Solution()

    testCase = [1,2,3,4,4,3,2,1]
    ans = solution.hasGroupsSizeX(testCase)
    print(f"test case 1: {ans} \n")

    testCase2 = [1,1,1,2,2,2,3,3]
    ans = solution.hasGroupsSizeX(testCase2)
    print(f"test case 2: {ans} \n")

    testCase3 = [1]
    ans = solution.hasGroupsSizeX(testCase3)
    print(f"test case 2: {ans} \n")