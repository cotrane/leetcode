from typing import List


class Solution:
    # Backtracking - Bottom Up
    def minCut(self, s: str) -> int:
        l = len(s)
        dp = [False] * (l+1)
        # Iterate over each character in s
        i, j = 0, l
        cut = 0
        while i < l and j > i:
            if s[i:l] == s[i:l][::-1]:
                i = j
                j = l
                cut += 1
            else:
                j -= 1
        return cut-1


if __name__ == "__main__":
    s, output = "aab", 1
    # s, output = "baab", 1
    # s, output = "a", 0

    print(s, output)
    print(Solution().minCut(s))