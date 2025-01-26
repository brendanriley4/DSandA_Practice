from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # We can do better!!!
        # Can not do greedy approach because of the test case [1, 4, 5] and amount being 12, would skip the [4, 4, 4] answer!
        # Bottom up tabulation!!
        coins.sort()
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            minn = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                minn = min(minn, dp[diff] + 1)

            dp[i] = minn

        if dp[amount] < float('inf'):
            return dp[amount]
        return -1


        # First top down memoization for the practice
        # coins.sort()
        # memo = {0:0}
        # def min_coins(amt):
        #     if amt in memo:
        #         return memo[amt]
        #     minn = float('inf')
        #     for coin in coins:
        #         diff = amt - coin
        #         if diff < 0:
        #             break
        #         minn = min(minn, 1 + min_coins(diff))
        #     memo[amt] = minn
        #     return minn
        #
        # result = min_coins(amount)
        # if result < float('inf'): return result
        # return -1

        # brute force recursion: can either give one kind of coin or not
        # min_num = [float('inf')]
        # def recurse(curr_num, cur_sum, index):
        #     if cur_sum == amount:
        #
        #         min_num[0] = min(min_num[0], curr_num)
        #         return
        #     if cur_sum > amount or index > len(coins) - 1:
        #         return
        #     recurse(curr_num + 1, cur_sum + coins[index], index)
        #     recurse(curr_num, cur_sum, index + 1)
        #
        # recurse(0, 0, 0)
        # return min_num[0] if min_num[0] != float('inf') else -1

if __name__ == '__main__':
    tc = [1,2,5]
    ta = 11
    solution = Solution()
    print(solution.coinChange(tc, ta))
