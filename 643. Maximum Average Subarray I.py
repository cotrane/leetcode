from typing import List
import unittest


class Solution:
    """You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average
    value and return this value. Any answer with a calculation error less than 10-5 will be
    accepted.
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Finds the maximum average value of a contiguous subarray of length k.

        Memory: O(1)
        Time: O(n)

        Args:
            nums (List[int]): The input array of integers.
            k (int): The length of the contiguous subarray to consider.

        Returns:
            float: The maximum average value of a contiguous subarray of length k.
        """
        curr_sum = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)
        return round(max_sum / float(k), 5)


class TestSolution(unittest.TestCase):
    def test_findMaxAverage(self):
        solution = Solution()
        self.assertEqual(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75)
        self.assertEqual(solution.findMaxAverage([5], 1), 5.0)
        self.assertEqual(solution.findMaxAverage([-1], 1), -1.0)
        self.assertEqual(solution.findMaxAverage([3, 3, 4, 3, 0], 3), 3.33333)


if __name__ == "__main__":
    unittest.main()
