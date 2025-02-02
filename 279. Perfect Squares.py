from typing import List


class SolutionRecursive:
    # Recursive - Runtime O(2^n) - Storage O(amt)
    def knapsackInf(self, i, amt, val, wt):
        if i == len(wt):
            return float('inf') if amt != 0 else 0

        take = float('inf')
        if wt[i] <= amt:
            take = val[i] + self.knapsackInf(i, amt - wt[i], val, wt)

        not_take = self.knapsackInf(i + 1, amt, val, wt)

        return min(take, not_take)

    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        perfectSquareNumbers = []
        i = 1
        while i**2 <= n:
            perfectSquareNumbers.append(i**2)
            i+=1

        count = self.knapsackInf(0, n, [1]*len(perfectSquareNumbers), perfectSquareNumbers)
        return count


class SolutionTopDown:
    # Top-Down using Memoization - Runtime O(n * amount) - Storage O(n * amount)
    def knapsackInf(self, i, amt, val, wt, mem):
        if i == len(wt):
            return float('inf') if amt != 0 else 0

        if mem[i][amt] != -1:
            return mem[i][amt]

        take = float('inf')
        if wt[i] <= amt:
            take = val[i] + self.knapsackInf(i, amt - wt[i], val, wt, mem)

        not_take = self.knapsackInf(i + 1, amt, val, wt, mem)

        mem[i][amt] = min(take, not_take)
        return mem[i][amt]

    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        perfectSquareNumbers = []
        i = 1
        while i**2 <= n:
            perfectSquareNumbers.append(i**2)
            i+=1
        mem = [[-1 for _ in range(n + 1)] for _ in range(len(perfectSquareNumbers))]
        count = self.knapsackInf(0, n, [1]*len(perfectSquareNumbers), perfectSquareNumbers, mem)
        return count



class SolutionBottomUp:
    # Bottom-Up Tabulation - Runtime O(n * amount) - Storage O(n * amount)
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        perfectSquareNumbers = []
        i = 1
        while i**2 <= n:
            perfectSquareNumbers.append(i**2)
            i+=1
        MAX = float('inf')
        ns = len(perfectSquareNumbers)
        dp = [[MAX for _ in range(n+1)] for _ in range(ns+1)]
        dp[0][0] = 0
        for i in range(1, ns+1):
            for j in range(n+1):
                dp[i][j] = min(dp[i][j - perfectSquareNumbers[i-1]] + 1, dp[i-1][j])
        return dp[ns][n]


class Solution:
    # Bottom-Up MemOptimized - Runtime O(n * amount) - Storage O(amount)
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        perfectSquareNumbers = []
        i = 1
        while i**2 <= n:
            perfectSquareNumbers.append(i**2)
            i+=1
        MAX = float('inf')
        ns = len(perfectSquareNumbers)
        dp = [0] + [MAX]*n
        for sq in perfectSquareNumbers:
            for curr_n in range(sq, n+1):
                dp[curr_n] = min(dp[curr_n], dp[curr_n - sq] + 1)
        return dp[n]


if __name__ == "__main__":
    n, output = 12, 3
    # n, output = 13, 2

    print(Solution().numSquares(n))

