class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1 = c2 = 0
        for x in cost[::-1]:
            c1, c2 = x + min(c1, c2), c1
        return min(c1, c2)