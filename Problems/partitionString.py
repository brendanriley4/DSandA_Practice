# Holy shit I just got my second medium done with no help first try, these have been pretty easy for mediums though lol

class Solution:
    def partitionString(self, s: str) -> int:
        numPar = 1
        mySet = set()
        for letter in s:
            if letter not in mySet:
                mySet.add(letter)
            else:
                numPar += 1
                mySet = set()
                mySet.add(letter)
        return numPar


if __name__ == '__main__':
    solution = Solution()

    testCase = "abacaba"
    ans = solution.partitionString(testCase)
    print(f"test case 1: {ans} \n")

    testCase2 = "ssssss"
    ans = solution.partitionString(testCase2)
    print(f"test case 2: {ans} \n")