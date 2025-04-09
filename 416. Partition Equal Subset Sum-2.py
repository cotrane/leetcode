import unittest
from typing import List


class SolutionRecursive:
    """Given an integer array nums, return true if you can partition the array into two subsets
    such that the sum of the elements in both subsets is equal or false otherwise.

    Memory: O(n)
    Time: O(2^n)
    """

    # Runtime: O(2**n), Space: O(n) - too slow
    def doSum(self, i, value, nums):
        if i < 0:
            return value == 0

        # add the value
        out1 = self.doSum(i - 1, value - nums[i], nums)
        # or don't add it
        out2 = self.doSum(i - 1, value, nums)

        return out1 or out2

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        half = sum(nums) // 2
        return self.doSum(len(nums) - 1, half, nums)


class SolutionBottomUp:
    """Given an integer array nums, return true if you can partition the array into two subsets
    such that the sum of the elements in both subsets is equal or false otherwise.

    Memory: O(n*half)
    Time: O(n*half)
    """

    # Runtime: O(n*half), Space: O(n*half)
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        # dp[i][j] represents if we can make sum j using first i numbers
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]

        # Base case: we can always make sum of 0
        for i in range(len(nums) + 1):
            dp[i][0] = True

        # For each number and each possible sum
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                if j < nums[i - 1]:  # can't use current number
                    dp[i][j] = dp[i - 1][j]
                else:  # can either use or not use current number
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[len(nums)][target]


class SolutionSpaceOptimized:
    """Given an integer array nums, return true if you can partition the array into two subsets
    such that the sum of the elements in both subsets is equal or false otherwise.

    Memory: O(n)
    Time: O(n*half)
    """

    # Runtime: O(half*half), Space: O(half)
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        half = sum(nums) // 2
        partition = [True] + [False for _ in range(half)]
        for n in nums:
            for m in range(half, n - 1, -1):
                partition[m] = partition[m] or partition[m - n]
        return partition[half]


class TestSolution(unittest.TestCase):
    def test_canPartition(self):
        solution = SolutionBottomUp()
        self.assertEqual(solution.canPartition([1, 5, 11, 5]), True)
        self.assertEqual(solution.canPartition([1, 2, 3, 5]), False)
        self.assertEqual(
            solution.canPartition(
                [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    99,
                    97,
                ]
            ),
            False,
        )
        self.assertEqual(solution.canPartition([3, 3, 3, 4, 5]), True)


if __name__ == "__main__":
    unittest.main()
