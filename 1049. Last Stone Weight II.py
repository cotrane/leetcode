from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half_sum = total // 2
        dp = [0 for _ in range(half_sum + 1)]
        for s in stones:
            for current_weight in range(half_sum, s-1, -1):
                # At each position, we want to take the maximum between:
                # (the current value at dp[current_weight]) and (the value at dp[current_weight - stone] + stone)
                # This represents either not taking the current stone or taking it and adding its weight to the subset.
                dp[current_weight] = max(dp[current_weight], dp[current_weight - s] + s)
        return total - (dp[-1] * 2)
        

if __name__ == "__main__":
    sample = [2,7,4,1,8,1]
    sample = [31,26,33,21,40]

    print(Solution().lastStoneWeightII(sample))