from typing import List

class SolutionBottomUp:
    # Bottom Up w Tabulation: runtime: O(n**2), storage O(n)
    def findNumberOfLIS(self, nums: List[int]) -> int:
        max_length = 1  # The length of the longest increasing subsequence
        answer = 0  # The number of longest increasing subsequences
        len_n = len(nums)
        dp = [1] * len_n
        max_len = [1] * len_n
        for i in range(1, len_n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j] + 1
                        max_len[i] = max_len[j]
                    elif dp[j] + 1 == dp[i]:
                        max_len[i] += max_len[j]
            if dp[i] > max_length:
                max_length = dp[i]
                answer = max_len[i]
            elif dp[i] == max_length:
                answer += max_len[i]
        return max(dp), sum(i for i, m in zip(max_len, dp) if m == max(dp))


if __name__ == "__main__":
    nums, output = [1,3,5,4,7], (4, 2)
    nums, output = [2,2,2,2,2], (1, 5)
    # nums, output = [1,3,2,5], (3, 2)
    # nums, output = [2,1,3,2,5], (3, 3)
    # nums, output = [10, 22, 9, 33, 21, 50, 41, 60], (5, 2)
    # nums, output = [1,1,1,2,2,2,3,3,3], (3, 27)
    # nums, output = [1,2,3,1,2,3,1,2,3], 10
    # nums, output = [1], 1
    print(nums, output)
    print(SolutionBottomUp().findNumberOfLIS(nums))
