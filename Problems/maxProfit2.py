class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # This was a foolish way to do this, you can just go from the front LOL
        # profit = 0
        # i = len(prices) - 2
        # jLim = len(prices) - 1
        # while i > -1:
        #     j = i + 1
        #     while j <= jLim:
        #         if prices[j] - prices[i] > 0:
        #             profit += prices[j] - prices[i]
        #             jLim = i
        #         j += 1
        #     i -= 1
        # return profit

        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit

if __name__ == '__main__':
    solution = Solution()

    testCase = [7,1,5,3,6,4]
    ans = solution.maxProfit(testCase)
    print(f"test case 1: {ans}")

    testCase2 = [1,2,3,4,5]
    ans = solution.maxProfit(testCase2)
    print(f"test case 2: {ans}")

    testCase3 = [7,6,4,3,1]
    ans = solution.maxProfit(testCase3)
    print(f"test case 3: {ans}")