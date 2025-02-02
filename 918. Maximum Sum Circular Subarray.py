from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s1 = s2 = f1 = f2 = nums[0]
        for num in nums[1:]:
            f1 = num + max(f1, 0)
            f2 = num + min(f2, 0)
            s1 = max(s1, f1)
            s2 = min(s2, f2)
        return s1 if s1 <= 0 else max(s1, sum(nums) - s2)

if __name__ == "__main__":
    sample = [-2,4,4,4,6]
    sample = [5,-3,5]
    sample = [-3,-2,-3]

    print(Solution().maxSubarraySumCircular(sample))