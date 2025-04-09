import unittest


class SolutionRecursion:
    """Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.

    Memory: O(1)
    Time: O(n^2)
    """

    def extendPalindrome(self, i, j, s):
        cnt = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            cnt += 1
            i -= 1
            j += 1
        return cnt

    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            # Odd length palindromes
            cnt += self.extendPalindrome(i, i, s)
            # Even length palindromes
            cnt += self.extendPalindrome(i, i + 1, s)
        return cnt


class SolutionBottomUp:
    """Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.

    Memory: O(n^2)
    Time: O(n^2)
    """

    def countSubstrings(self, s: str) -> int:
        count = 0
        # Check for palindromes of all lengths from 1 to len(s)
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for l in range(1, len(s) + 1):  # Check for palindromes of length l
            for start in range(len(s) - l + 1):  # Start of the substring
                end = start + l - 1  # End of the substring
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    count += 1
        return count


class TestSolution(unittest.TestCase):
    def test_countSubstrings(self):
        solution = SolutionBottomUp()
        self.assertEqual(solution.countSubstrings("abc"), 3)
        self.assertEqual(solution.countSubstrings("aaa"), 6)
        self.assertEqual(solution.countSubstrings("aabbcc"), 9)
        self.assertEqual(solution.countSubstrings("aaaaa"), 15)
        self.assertEqual(solution.countSubstrings("fdsklf"), 6)
        self.assertEqual(solution.countSubstrings("aba"), 4)
        self.assertEqual(solution.countSubstrings("xabax"), 7)
        self.assertEqual(solution.countSubstrings("xabaxy"), 8)


if __name__ == "__main__":
    unittest.main()
