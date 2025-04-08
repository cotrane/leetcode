from typing import List


class Solution:
    """Solves the maximum product subarray problem:

    Given an integer array nums, find a contiguous non-empty subarray within the array
    that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.
    """

    def maxProduct(self, nums: List[int]) -> int:
        """Finds the maximum product of a contiguous subarray in nums.

        Memory: O(1)
        Time: O(n)

        Args:
            nums (List[int]): list of integers

        Returns:
            int: maximum product of a contiguous subarray in nums
        """
        max_prod = min_prod = ans = nums[0]
        for n in nums[1:]:
            # print(f"n = {n}")
            tmp_max_prod = max_prod
            max_prod = max(max_prod * n, n) if n > 0 else max(min_prod * n, n)
            # print(f"p1 = {p1}, {max(p2 * n, n)}")
            min_prod = min(min_prod * n, n) if n > 0 else min(tmp_max_prod * n, n)
            # print(f"p2 = {p2}, {min(p1 * n, n)}")
            ans = max(ans, max_prod)
        return ans


if __name__ == "__main__":
    sample = [2, 3, -2, 4]
    sample = [-2, 0, -1]
    sample = [2, 3, -2, -4]
    sample = [2, 0, -2, -4]

    print(Solution().maxProduct(sample))
