from typing import List


class SolutionBinarySearch:
    # Runtime O(NlogN), Memory O(N)
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # we need to sort first in order to be able to handle the 
        # separate dimension
        # notice the '-' sign for the second element; this guarantees
        # that the larger one appears first; if there is subsequently a 
        # smaller one for the y dim, it will replace the larger element
        # instead of append
        envs = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        num_env = len(envs)
        tails = [envs[0]]
        for i in range(1, num_env):

            if envs[i][1] > tails[-1][1]:
                tails.append(envs[i])

            else:
                # binary search
                low = 0
                high = len(tails) - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if tails[mid][1] >= envs[i][1]:
                        high = mid
                    else:
                        low = mid+1
                tails[low] = envs[i]

        return len(tails)



if __name__ == "__main__":
    nums, output = [[5,4],[6,4],[6,7],[2,3]], 3
    # nums, output = [[1,1],[1,1],[1,1]], 1
    # nums, output = [[8,8],[6,4],[6,9],[2,3]], 3
    # nums, output = [[8,8],[6,3],[2,3]], 2
    nums, output = [[1,1]], 1
    nums, output = [], 0
    nums, output = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]], 5
    print(nums, output)
    print(SolutionBinarySearch().maxEnvelopes(nums))
