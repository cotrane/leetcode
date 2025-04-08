import unittest
from typing import List


class Solution:
    """The DNA sequence is composed of a series of nucleotides abbreviated as
    'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.
    When studying DNA, it is useful to identify repeated sequences within the DNA.

    Given a string s that represents a DNA sequence, return all the 10-letter-long
    sequences (substrings) that occur more than once in a DNA molecule. You may return
    the answer in any order.
    """

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """Finds all the 10-letter-long sequences (substrings) that occur more than
        once in a DNA molecule.

        Memory: O(n)
        Time: O(n)
        """
        if len(s) < 10:
            return []
        seen = set()
        result = set()
        for i in range(len(s) - 9):
            seq = s[i : i + 10]
            if seq in seen:
                result.add(seq)
            else:
                seen.add(seq)
        return list(result)


class TestSolution(unittest.TestCase):
    def test_findRepeatedDnaSequences(self):
        solution = Solution()
        self.assertSetEqual(
            set(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")),
            {"AAAAACCCCC", "CCCCCAAAAA"},
        )
        self.assertSetEqual(
            set(solution.findRepeatedDnaSequences("AAAAAAAAAAAAA")), {"AAAAAAAAAA"}
        )


if __name__ == "__main__":
    unittest.main()
