from typing import List

class Solution:
	# Runtime O(t1 * t2) - Storage O(t1 * t2)
    def minDistance(self, text1: str, text2: str) -> int:
    	dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
    	max_sseq = 0
    	for i, c1 in enumerate(text1):
    		for j, c2 in enumerate(text2):
    			if c1 == c2:
    				dp[i][j] = dp[i-1][j-1] + 1
    			else:
    				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    			if max_sseq < dp[i][j]:
    				max_sseq = dp[i][j]
    	return len(text1) + len(text2) - 2*max_sseq



if __name__ == "__main__":
    text1, text2, output = "sea", "eat", 2
    # text1, text2, output = "leetcode", "etco", 4

    print(Solution().minDistance(text1, text2))