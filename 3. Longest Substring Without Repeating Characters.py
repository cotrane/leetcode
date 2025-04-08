import unittest


class Solution:
    """Given a string s, find the length of the longest substring without duplicate characters."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        """Finds the length of the longest substring without duplicate characters.

        Memory: O(n)
        Time: O(n)

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without duplicate characters.
        """
        left = right = 0
        char_set = set()
        max_len = 0
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                max_len = max(max_len, right - left)
            else:
                char_set.remove(s[left])
                left += 1
        return max_len


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
