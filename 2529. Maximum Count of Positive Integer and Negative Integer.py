import unittest
from typing import List


class Solution:
    """Given an array nums sorted in non-decreasing order, return the maximum between the number
    of positive integers and the number of negative integers.

    In other words, if the number of positive integers in nums is pos and the number of negative
    integers is neg, then return the maximum of pos and neg.
    Note that 0 is neither positive nor negative.
    """

    def maximumCount(self, nums: List[int]) -> int:
        """Finds the maximum count of positive and negative integers in a sorted array.

        Args:
            nums (List[int]): The sorted array of integers.

        Returns:
            int: The maximum count of positive and negative integers in the array.
        """

        def binary_search(nums: List[int], target: int) -> int:
            """Finds the first occurrence of a value equal or greater than a target value
            in a sorted array using binary search.

            Args:
                nums (List[int]): The sorted array of integers.
                target (int): The target value to search for.

            Returns:
                int: The index of the first occurrence of the value equal or greater than
                the target value.
            """
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        left = binary_search(nums, 0)
        right = binary_search(nums, 1)
        return max(left, len(nums) - right)


class TestSolution(unittest.TestCase):
    def test_maximumCount(self):
        solution = Solution()
        self.assertEqual(solution.maximumCount([-3, -2, -1, 0, 0, 1, 2]), 3)
        self.assertEqual(solution.maximumCount([-2, -1, -1, 1, 2, 3]), 3)
        self.assertEqual(solution.maximumCount([5, 20, 66, 1314]), 4)
        self.assertEqual(solution.maximumCount([0, 0]), 0)


if __name__ == "__main__":
    unittest.main()
