from typing import List


class SolutionTooSlow:
    def napsack(self, idx, a, nums, target):
        if idx == len(nums):
            return int(a == target)
        
        opt_1 = self.napsack(idx+1, a+nums[idx], nums, target)
        opt_2 = self.napsack(idx+1, a-nums[idx], nums, target)

        return opt_1 + opt_2

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.napsack(0, 0, nums, target)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target or (s - target) % 2 != 0:
            return 0

        subsum = (s - target) // 2
        dp = [1] + [0 for _ in range(subsum)]
        for n in nums:
            for i in range(subsum, n-1, -1):
                dp[i] = dp[i] + dp[i - n]
        return dp[-1]
        

if __name__ == "__main__":
    sample, target = [1,1,1,1,1], 3
    # sample, target = [1], 1
    # sample, target = [2, 1], 1
    sample, target = [38,7,5,14,29,26,35,35,42,48,14,32,5,1,39,50,3,34,38,10], 49

    print(Solution().findTargetSumWays(sample, target))