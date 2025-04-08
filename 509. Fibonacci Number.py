class SolutionWithMemoization:
    fib_dict: dict[int, int] = {}

    def fib(self, n: int) -> int:
        """Solves the Fibonacci problem using memoization

        Memory: O(n)
        Time: O(n)

        Args:
            n (int): number of the Fibonacci sequence

        Returns:
            int: the nth Fibonacci number
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.fib_dict:
            return self.fib_dict[n]
        self.fib_dict[n - 1] = self.fib(n - 1)
        self.fib_dict[n - 2] = self.fib(n - 2)
        return self.fib_dict[n - 1] + self.fib_dict[n - 2]


class SolutionBottomUp:
    def fib(self, n: int) -> int:
        """Solves the Fibonacci problem using bottom-up dynamic programming

        Memory: O(1)
        Time: O(n)

        Args:
            n (int): number of the Fibonacci sequence

        Returns:
            int: the nth Fibonacci number
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev_1 = 0
        prev_2 = 1
        for _ in range(2, n + 1):
            prev_1, prev_2 = prev_2, prev_1 + prev_2
        return prev_2
