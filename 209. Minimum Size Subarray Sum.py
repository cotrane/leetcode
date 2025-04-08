from typing import List


class Solution:
    """Given an array of positive integers nums and a positive integer target, return the minimal
    length of a subarray whose sum is greater than or equal to target. If there is no such subarray,
    return 0 instead.
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Finds the minimal length of a subarray whose sum is greater than or equal to target.

        Memory: O(1)
        Time: O(n)
        """
        min_length = float("inf")
        left = curr_sum = 0
        for right, n in enumerate(nums):
            curr_sum += n
            if curr_sum >= target:
                while (curr_sum - nums[left]) >= target:
                    curr_sum -= nums[left]
                    left += 1
                min_length = min(min_length, right - left + 1)
        return min_length if min_length != float("inf") else 0
