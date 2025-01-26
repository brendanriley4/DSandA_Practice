# This is my first time solving a medium difficulty on my first try with no help, the new monitor setup is good luck!!!

class Solution:
    def kthFactor(self, n, k):
        factors = []
        for num in range(1, (n//2) + 1, 1):
            if n % num == 0:
                factors.append(num)
        factors.append(n)
        if len(factors) < k: return -1
        return factors[k - 1]



if __name__ == '__main__':
    solution = Solution()

    testCase = 12
    n1 = 3
    ans = solution.kthFactor(testCase, n1)
    print(f"test case 1: {ans} \n")

    testCase2 = 7
    n2 = 2
    ans = solution.kthFactor(testCase2, n2)
    print(f"test case 2: {ans} \n")

    testCase3 = 4
    n3 = 4
    ans = solution.kthFactor(testCase3, n3)
    print(f"test case 3: {ans} \n")