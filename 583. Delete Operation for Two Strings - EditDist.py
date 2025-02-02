
class Solution:
    # Solve the problem using editDistance approach without the replace operation
    def minDistance(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(l1+1):
            dp[i][0] = i
        for j in range(l2+1):
            dp[0][j] = j
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        # for d in dp:
        #     print(d)
        return dp[l1][l2]



if __name__ == "__main__":
    text1, text2, output = "sea", "eat", 2
    # text1, text2, output = "intention", "execution", 5
    # text1, text2, output = "cat", "cut", 1
    # text1, text2, output = "saturday", "sunday", 3
    # text1, text2, output = "GEEXSFRGEEKKS", "GEEKSFORGEEKS", 3
    # text1, text2, output = "a", "b", 1

    print(text1, text2, output)
    print(Solution().minDistance(text1, text2))