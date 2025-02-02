from typing import List

class SolutionBottomUp:
    # Bottom Up w Tabulation: runtime: O(n**2), storage O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_n = len(nums)
        dp = [1] * len_n
        for i in range(1, len_n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

class SolutionBinarySearch:
    # Bottom Up w Tabulation: runtime: O(nlogn), storage O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_n = len(nums)
        ans = [nums[0]]
        for i in range(1, len_n):
            # if the current number is larger than the previous
            # on in the subsequence, append it
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            # otherwise we try to find the smallest element
            # in ans which is greater than or equal to the 
            # current element (binary search)
            else:
                low = 0
                high = len(ans) - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if ans[mid] < nums[i]:
                        low = mid + 1
                    else:
                        high = mid
                # Once we found that element, we update the
                # element at that position with the current
                # element to maintain a sorted list
                ans[low] = nums[i]
        return len(ans)




if __name__ == "__main__":
    nums, output = [10,9,2,5,3,7,101,18], 4
    # nums, output = [0,1,0,3,2,3], 4
    # nums, output = [7,7,7,7,7,7,7], 4
    # nums, output = [1,3,2,5], 3
    # nums, output = [2,1,3,2,5], 3
    # nums, output = [10, 22, 9, 33, 21, 50, 41, 60], 5
    print(nums, output)
    print(SolutionBinarySearch().lengthOfLIS(nums))
