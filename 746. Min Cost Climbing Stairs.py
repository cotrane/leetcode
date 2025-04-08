class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """Solves the min cost climbing stairs problem

        Memory: O(1)
        Time: O(n)

        Args:
            cost (list[int]): cost of climbing stairs

        Returns:
            int: minimum cost to reach the top of the stairs
        """
        c1 = c2 = 0
        for x in cost[::-1]:
            c1, c2 = x + min(c1, c2), c1
        return min(c1, c2)
