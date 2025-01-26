class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i > 0 or j > 0 or carry:
            aDig = int(a[i]) if i <len(a) - 1 else 0
            bDig = int(b[i]) if i <len(b) - 1 else 0

            total = aDig + bDig + carry
            carry = total // 2
            res.append(str(total % 2))

            i -= 1
            j -= 1

        return ''.join(res[::-1])

if __name__ == '__main__':
    solution = Solution()

    testCase = "11"
    test = "101"
    ans = solution.addBinary(testCase, test)
    print(f"test case 1: {ans} \n")

    testCase2 = "1010"
    test2 = "1011"
    ans = solution.addBinary(testCase2, test2)
    print(f"test case 2: {ans} \n")
