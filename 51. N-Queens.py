import unittest
from typing import List


class Solution:
    """The n-queens puzzle is the problem of placing n queens on an n x n chessboard such
    that no two queens attack each other.

    Given an integer n, return all distinct solutions to the n-queens puzzle. You may return
    the answer in any order.

    Each solution contains a distinct board configuration of the n-queens' placement,
    where 'Q' and '.' both indicate a queen and an empty space, respectively.

    Memory: O(n^2)
    Time: O(n^2)
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]
        col = [0 for _ in range(n)]
        pos_diag = [0 for _ in range(2 * n - 1)]
        neg_diag = [0 for _ in range(2 * n - 1)]

        def backtrack(row):
            # If row is n, we have a solution
            if row == n:
                result.append(["".join(row) for row in board])
                return
            # Otherwise, we try to place a queen in each column
            for c in range(n):
                # If the column is already occupied, or the position is already occupied, skip
                if col[c] or pos_diag[row + c] or neg_diag[row - c]:
                    continue

                # Place the queen
                board[row][c] = "Q"
                col[c] = 1
                pos_diag[row + c] = 1
                neg_diag[row - c] = 1

                # Recurse
                backtrack(row + 1)

                # Backtrack
                board[row][c] = "."
                col[c] = 0
                pos_diag[row + c] = 0
                neg_diag[row - c] = 0

            # If we have tried all columns and still no solution, return
            return

        backtrack(0)
        return result


class TestSolution(unittest.TestCase):
    def test_solveNQueens(self):
        self.assertEqual(
            Solution().solveNQueens(4),
            [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
        )
        self.assertEqual(Solution().solveNQueens(1), [["Q"]])
        self.assertEqual(Solution().solveNQueens(2), [])
        self.assertEqual(Solution().solveNQueens(3), [])


if __name__ == "__main__":
    unittest.main()
