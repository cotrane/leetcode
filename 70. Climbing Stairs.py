class SolutionWithMemoization:
    steps_dict: dict[int, int] = {}

    def climbStairs(self, n: int) -> int:
        """Solves the climbing stairs problem using memoization

        Memory: O(n)
        Time: O(n)

        Args:
            n (int): number of stairs

        Returns:
            int: number of ways to climb the stairs
        """
        if n == 2:
            return 2
        if n == 1:
            return 1
        if n in self.steps_dict:
            return self.steps_dict[n]

        self.steps_dict[n - 1] = self.climbStairs(n - 1)
        self.steps_dict[n - 2] = self.climbStairs(n - 2)
        return self.steps_dict[n - 1] + self.steps_dict[n - 2]


class SolutionBottomUp:
    def climbStairs(self, n: int) -> int:
        """Solves the climbing stairs problem using bottom-up dynamic programming

        Memory: O(1)
        Time: O(n)

        Args:
            n (int): number of stairs

        Returns:
            int: number of ways to climb the stairs
        """
        if n == 2:
            return 2
        if n == 1:
            return 1

        prev_1 = 1
        prev_2 = 2
        for _ in range(3, n + 1):
            prev_1, prev_2 = prev_2, prev_1 + prev_2
        return prev_2
