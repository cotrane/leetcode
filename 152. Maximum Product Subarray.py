from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p1 = p2 = m1 = nums[0]
        for n in nums[1:]:
            # print(f"n = {n}")
            tmp_p1 = p1
            p1 = max(p1 * n, n) if n > 0 else max(p2 * n, n)
            # print(f"p1 = {p1}, {max(p2 * n, n)}")
            p2 = min(p2 * n, n) if n > 0 else min(tmp_p1 * n, n)
            # print(f"p2 = {p2}, {min(p1 * n, n)}")
            m1 = max(p1, m1)
        return m1

if __name__ == "__main__":
    sample = [2,3,-2,4]
    sample = [-2,0,-1]
    sample = [2,3,-2,-4]
    sample = [2,0,-2,-4]

    print(Solution().maxSubarraySumCircular(sample))