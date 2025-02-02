from typing import List

class SolutionSpaceOptimized:
    # Runtime: O(n*hs) Space: O(hs)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target or (s - target) % 2 != 0:
            return 0

        hs = (s - target) // 2
        dp = [1] + [0 for _ in range(hs)]
        for n in nums:
            for m in range(hs, n-1, -1):
                dp[m] = dp[m] + dp[m-n]
        return dp[-1]


if __name__ == "__main__":
    nums, target, output = [1,1,1,1,1], 3, 5
    nums, target, output = [1], 1, 1
    nums, target, output = [2, 1], 1, 1
    nums, target, output = [38,7,5,14,29,26,35,35,42,48,14,32,5,1,39,50,3,34,38,10], 49, 5706

    print(nums, target, output)
    print(SolutionSpaceOptimized().findTargetSumWays(nums, target))
