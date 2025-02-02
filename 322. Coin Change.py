from typing import List


class SolutionRecursive:
    # Recursive - Runtime O(2^n) - Storage O(amt)
    def knapsackInf(self, i, amt, val, wt):
        if i == len(coins):
            return 0 if amt == 0 else float('inf')

        take = float('inf')
        if coins[i] <= amt:
            take = val[i] + self.knapsackInf(i, amt - wt[i], val, wt)

        not_take = self.knapsackInf(i + 1, amt, val, wt)

        print(i, amt, take, not_take)
        return min(take, not_take)

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        count = self.knapsackInf(0, amount, [1]*len(coins), coins)
        return -1 if count == float('inf') else count


class SolutionTopDown:
    # Top-Down using Memoization - Runtime O(n * amount) - Storage O(n * amount)
    def knapsackInf(self, i, amt, val, wt, mem):
        if i == len(coins):
            return 0 if amt == 0 else float('inf')

        if mem[i][amt] != -1:
            return mem[i][amt]

        take = float('inf')
        if coins[i] <= amt:
            take = val[i] + self.knapsackInf(i, amt - wt[i], val, wt, mem)

        not_take = self.knapsackInf(i + 1, amt, val, wt, mem)

        mem[i][amt] = min(take, not_take)
        print(i, amt, take, not_take)
        return mem[i][amt]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        mem = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        count = self.knapsackInf(0, amount, [1]*len(coins), coins, mem)
        return -1 if count == float('inf') else count



class SolutionBottomUp:
    # Bottom-Up Tabulation - Runtime O(n * amount) - Storage O(n * amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        MAX = float('inf')
        dp = [[MAX for _ in range(amount+1)] for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(amount+1):
                if (j - coins[i-1]) >= 0:
                    # if the amount j - the current coin is larger 0
                    # add the min between not using the coin and using the coin
                    dp[i][j] = min(dp[i-1][j], dp[i][j - coins[i-1]]+1)
                else:
                    # otherwise, add the case of not using the coin
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount] if dp[n][amount] < MAX else -1


class Solution:
    # Bottom-Up MemOptimized - Runtime O(n * amount) - Storage O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        MAX = float('inf')
        dp = [0] + [MAX]*amount
        for coin in coins:
            for curr_amt in range(coin, amount+1):
                dp[curr_amt] = min(dp[curr_amt], dp[curr_amt - coin] + 1)
        return -1 if dp[amount] == MAX else dp[amount]


if __name__ == "__main__":
    coins, amount, output = [1,2,5], 11, 3
    # coins, amount, output = [1,2,5], 5, 1
    coins, amount, output = [2], 3, -1
    coins, amount, output = [1], 0, 0

    print(SolutionBottomUp().coinChange(coins, amount))

