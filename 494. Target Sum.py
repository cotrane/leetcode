from typing import List
import unittest


class SolutionTooSlow:
    """This solution is too slow because it has a time complexity of O(2^n)."""

    def napsack(self, idx, a, nums, target):
        """Finds the number of different expressions that you can build, which evaluates to target.

        Memory: O(n)
        Time: O(2^n)

        Args:
            idx (int): index of the current element
            a (int): current sum
            nums (List[int]): list of integers
            target (int): target sum

        Returns:
            int: number of different expressions that you can build, which evaluates to target
        """
        if idx == len(nums):
            return int(a == target)

        opt_1 = self.napsack(idx + 1, a + nums[idx], nums, target)
        opt_2 = self.napsack(idx + 1, a - nums[idx], nums, target)

        return opt_1 + opt_2

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Finds the number of different expressions that you can build, which evaluates to target.

        Memory: O(n)
        Time: O(2^n)
        """
        return self.napsack(0, 0, nums, target)


class Solution:
    """You are given an integer array nums and an integer target.

    You want to build an expression out of nums by adding one of the symbols '+' and '-'
    before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate
    them to build the expression "+2-1".

    Return the number of different expressions that you can build, which evaluates to target.
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Finds the number of different expressions that you can build, which evaluates to target.

        Memory: O(n)
        Time: O(n)

        Args:
            nums (List[int]): list of integers
            target (int): target sum

        Returns:
            int: number of different expressions that you can build, which evaluates to target
        """
        s = sum(nums)
        if s < target or (s - target) % 2 != 0:
            return 0

        subsum = (s - target) // 2
        dp = [1] + [0 for _ in range(subsum)]
        for n in nums:
            for i in range(subsum, n - 1, -1):
                dp[i] = dp[i] + dp[i - n]
        return dp[-1]


class TestSolution(unittest.TestCase):
    def test_findTargetSumWays(self):
        solution = Solution()
        self.assertEqual(solution.findTargetSumWays([1, 1, 1, 1, 1], 3), 5)
        self.assertEqual(solution.findTargetSumWays([1], 1), 1)
        self.assertEqual(solution.findTargetSumWays([2, 1], 1), 1)
        self.assertEqual(
            solution.findTargetSumWays(
                [
                    38,
                    7,
                    5,
                    14,
                    29,
                    26,
                    35,
                    35,
                    42,
                    48,
                    14,
                    32,
                    5,
                    1,
                    39,
                    50,
                    3,
                    34,
                    38,
                    10,
                ],
                49,
            ),
            1,
        )


if __name__ == "__main__":
    unittest.main()
