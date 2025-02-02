class Solution:
    fib_dict = {}

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.fib_dict:
            return self.fib_dict[n]
        return self.fib(n-1) + self.fib(n-2)