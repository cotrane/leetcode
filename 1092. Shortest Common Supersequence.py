from typing import List
from pprint import PrettyPrinter

class Solution:
    # Runtime O(t1 * t2) - Storage O(t1 * t2)
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        scss = []
        i, j = n, m
        while i > 0 or j > 0:
            if i == 0:
                j -= 1
                scss.append(text2[j])
            elif j == 0:
                i -= 1
                scss.append(text1[i])
            else:
                if dp[i][j] == dp[i-1][j]:
                    i -= 1
                    scss.append(text1[i])
                elif dp[i][j] == dp[i][j-1]:
                    j -= 1
                    scss.append(text2[j])
                else:
                    i -=1
                    j -= 1
                    scss.append(text1[i])
        return "".join(scss[::-1])



if __name__ == "__main__":
    text1, text2, output = "abac", "cab", "cabac"
    # text1, text2, output = "aaaaaaaa", "aaaaaaaa", "aaaaaaaa"
    text1, text2, output = "bbbaaaba", "bbababbb", "bbbaaababbb"
    text1, text2, output = "geek", "eke", "geeke"
    text1, text2, output = "AGGTAB", "GXTXAYB", "AGXGTXAYB"

    print(Solution().shortestCommonSupersequence(text1, text2))