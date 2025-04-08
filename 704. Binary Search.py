import unittest
from typing import List


class Solution:
    """Given an array of integers nums which is sorted in ascending order, and an integer target,
    write a function to search target in nums. If target exists, then return its index.
    Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
    """

    def search(self, nums: List[int], target: int) -> int:
        """Searches for a target value in a sorted array using binary search.

        Memory: O(1)
        Time: O(log n)

        Args:
            nums (List[int]): The sorted array of integers.
            target (int): The target value to search for.

        Returns:
            int: The index of the target value in the array, or -1 if the target value is not present.
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return right if nums[right] == target else -1


class TestSolution(unittest.TestCase):
    def test_search(self):
        solution = Solution()
        self.assertEqual(solution.search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(solution.search([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == "__main__":
    unittest.main()
