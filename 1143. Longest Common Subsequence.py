import unittest

class Solution:
    """Given two strings text1 and text2, return the length of their longest common subsequence. 
    If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original string with some 
    characters (can be none) deleted without changing the relative order of the remaining 
    characters.

    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.

    Memory: O(t1 * t2)
    Time: O(t1 * t2)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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
		return max_sseq


class TestSolution(unittest.TestCase):
    def test_longestCommonSubsequence(self):
        self.assertEqual(Solution().longestCommonSubsequence("abcde", "ace"), 3)
        self.assertEqual(Solution().longestCommonSubsequence("abc", "abc"), 3)
        self.assertEqual(Solution().longestCommonSubsequence("abc", "def"), 0)


if __name__ == "__main__":
    unittest.main()
