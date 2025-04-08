class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """Solves the maximum sum circular subarray problem:

        Given a circular integer array nums of length n, return the maximum possible
        sum of a non-empty subarray of nums.

        A circular array means the end of the array connects to the beginning of the
        array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous
        element of nums[i] is nums[(i - 1 + n) % n].

        A subarray may only include each element of the fixed buffer nums at most once.
        Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist
        i <= k1, k2 <= j with k1 % n == k2 % n.

        Memory: O(1)
        Time: O(n)

        Args:
            nums (list[int]): list of integers

        Returns:
            int: maximum sum of a non-empty subarray of nums
        """
        max_sum = curr_max = nums[0]
        min_sum = curr_min = nums[0]
        for num in nums[1:]:
            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)
        # If all numbers are negative, return the maximum sum
        # Otherwise, return the maximum of the non-wrapped case or the wrapped case
        # (sum of whole array - minimum subarray sum)
        return max_sum if max_sum <= 0 else max(max_sum, sum(nums) - min_sum)


if __name__ == "__main__":
    sample = [-2, 4, 4, 4, 6]
    sample = [5, -3, 5]
    sample = [-3, -2, -3]

    print(Solution().maxSubarraySumCircular(sample))
