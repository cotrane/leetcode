from typing import List


class Solution:
    """Given a binary array nums, return the maximum length of a contiguous
    subarray with an equal number of 0 and 1.
    """

    def findMaxLength(self, nums: List[int]) -> int:
        """Finds the maximum length of a contiguous subarray with an equal number of 0 and 1.

        Memory: O(n)
        Time: O(n)
        """
        count = max_length = 0
        count_map = {0: -1}

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i
        return max_length
