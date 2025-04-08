from typing import List


class Solution:
    """Given an array of integers nums and an integer k, return the total number of
    subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        """Finds the total number of subarrays whose sum equals to k.

        Memory: O(n)
        Time: O(n)
        """
        count = num_subarrays = 0
        count_map = {0: 1}

        for n in nums:
            count += n

            if count - k in count_map:
                num_subarrays += count_map[count - k]

            if count in count_map:
                count_map[count] = count_map[count] + 1
            else:
                count_map[count] = 1
        return num_subarrays
