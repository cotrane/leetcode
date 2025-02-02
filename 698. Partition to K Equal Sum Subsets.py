from typing import List


class Solution:
    # Runtime: O(k**n) Space: O(n+k)
    def search(self, subset_sums: List[int], index: int, target_sum: int, nums: List[int]) -> bool:
        if index == len(nums):
            return True

        # Iterate over subsets and do depth first search
        for j in range(len(subset_sums)):
            # If the previous subset_sum is identical to the current, skip recursion
            if j > 0 and subset_sums[j] == subset_sums[j-1]:
                continue
            subset_sums[j] += nums[index]
            # Recurse only if the current subset sum is less than or equal to target subset
            if subset_sums[j] <= target_sum and self.search(subset_sums, index+1, target_sum, nums):
                return True
            # Otherwise backtrack
            subset_sums[j] -= nums[index]
        # If nothing worked, return False
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False

        target = s // k
        subset_sums = [0] * k
        nums = sorted(nums, reverse=True)
        return self.search(subset_sums, 0, target, nums)


if __name__ == "__main__":
    nums, k, output = [4,3,2,3,5,2,1], 4, True
    nums, k, output = [1,2,3,4], 3, False

    print(nums, output)
    print(Solution().canPartitionKSubsets(nums, k))