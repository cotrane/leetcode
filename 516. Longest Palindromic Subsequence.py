

class SolutionLCS:
	# Solve like longest common subsequence of string and inverse string
	# Runtime: O(N**2), Storage O(N**2)
    def longestPalindromeSubseq(self, s: str) -> int:
    	len_s = len(s)
    	s_inv = s[::-1]
    	dp = [[0 for _ in range(len_s + 1)] for _ in range(len_s + 1)]
    	max_sseq = 0
    	for i in range(len_s):
    		for j in range(len_s):
    			if s[i] == s_inv[j]:
    				dp[i][j] = dp[i-1][j-1] + 1
    			else:
    				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    			if max_sseq < dp[i][j]:
    				max_sseq = dp[i][j]
    	return max_sseq


class SolutionRecursion:
	# Solve recursively with memoization
	# Runtime: O(N**2), Storage O(N**2)
    def pss(self, i, j, s, cache):
        if i < 0 or j == len(s):
            return 0

        if (i, j) in cache:
            return cache[(i, j)]

        if s[i] == s[j]:
            length = 1 if i == j else 2
            cache[(i, j)] = length + self.pss(i-1, j+1, s, cache)
        else:
            # shift left
            out1 = self.pss(i-1, j, s, cache)
            # or shift right
            out2 = self.pss(i, j+1, s, cache)
            cache[(i, j)] = max(out1, out2)
        return cache[(i, j)]

    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        lpss = 0
        for i in range(len(s)):
            self.pss(i, i, s, cache)
            self.pss(i, i+1, s, cache)
        return max(cache.values())


class SolutionBottomUp:
    # Solve differently
    # Runtime: O(N**2), Storage O(N**2)
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        res = 0
        # The for loops need to start from opposite ends to test for a 
        # palindrome!
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if i == j else 2
                    if i - 1 >= 0:
                        dp[i][j] += dp[i-1][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
                res = max(res, dp[i][j])
        return res



if __name__ == "__main__":
    s, output = "bbbab", 4
    # s, output = "cbbd", 2
    print(s, output)
    print(SolutionBottomUp().longestPalindromeSubseq(s))



