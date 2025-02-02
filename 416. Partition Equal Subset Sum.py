from typing import List


class SolutionTooSlow:
    """This solution is not efficient enough"""
    def knapsack(self, idx, a, b, nums):
        # if we are at the end of the list, check if the 2 bags are equal
        if idx == len(nums):
            return a == b
        # otherwise, add it to bag a
        opt_a = self.knapsack(idx+1, a + nums[idx], b, nums)
        # or bag b
        opt_b = self.knapsack(idx+1, a, b + nums[idx], nums)
        return opt_a or opt_b

    def canPartition(self, nums: List[int]) -> bool:
        return self.knapsack(0, 0, 0, nums)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        half_sum = s // 2
        print(f"half_sum: {half_sum}")
        isPossible = [True] + [False for _ in range(half_sum)]
        for n in nums:
            print(f"n = {n}")
            for i in range(half_sum, n-1, -1):
                isPossible[i] = isPossible[i] or isPossible[i - n]
                print(f"{i}: {isPossible}")
        return isPossible[half_sum]
        

if __name__ == "__main__":
    # sample = [1,5,11,5]
    # sample = [1,2,3,5]
    sample = [5,1,2]
    # sample = [2,2,1,1]
    # sample = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
    sample, output = [3,3,3,4,5], True
    
    print(Solution().canPartition(sample))