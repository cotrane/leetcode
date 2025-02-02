from typing import List


class SolutionRecursive:
    # Recursive - Runtime O(2^n) - Storage O(amt)
    def knapsackInf(self, i, amt, val, wt):
        if i == len(wt):
            return 0 if amt != 0 else 1

        take = 0
        if wt[i] <= amt:
            take = self.knapsackInf(i, amt - wt[i], val, wt)

        not_take = self.knapsackInf(i + 1, amt, val, wt)

        return take + not_take

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 1
        count = self.knapsackInf(0, amount, [1]*len(coins), coins)
        return count


class SolutionTopDown:
    # Top-Down using Memoization - Runtime O(n * amount) - Storage O(n * amount)
    def knapsackInf(self, i, amt, val, wt, mem):
        if i == len(wt):
            return 0 if amt != 0 else 1

        if mem[i][amt] != -1:
            return mem[i][amt]

        take = 0
        if wt[i] <= amt:
            take = self.knapsackInf(i, amt - wt[i], val, wt, mem)

        not_take = self.knapsackInf(i + 1, amt, val, wt, mem)

        mem[i][amt] = take + not_take
        return mem[i][amt]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 1
        mem = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        count = self.knapsackInf(0, amount, [1]*len(coins), coins, mem)
        return count



class SolutionBottomUp:
    # Bottom-Up Tabulation - Runtime O(n * amount) - Storage O(n * amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 1
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(amount+1):
                if (j - coins[i-1]) >= 0:
                    # if the amount j - the current coin is larger or equal 0
                    # add up ways to reach the amount with and without the current coin
                    dp[i][j] += dp[i][j - coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] += dp[i-1][j]
        print(dp)
        return dp[n][amount]


class Solution:
    # Bottom-Up MemOptimized - Runtime O(n * amount) - Storage O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 1
        dp = [1] + [0]*amount
        for coin in coins:
            for curr_amt in range(coin, amount+1):
                dp[curr_amt] = dp[curr_amt] + dp[curr_amt - coin]
        print(dp)
        return dp[amount]


if __name__ == "__main__":
    coins, amount, output = [1,2,5], 5, 4
    coins, amount, output = [2], 3, 0
    coins, amount, output = [10], 10, 1

    print(Solution().coinChange(coins, amount))

