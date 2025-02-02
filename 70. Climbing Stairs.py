class Solution:
    steps_dict = {}
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        elif n == 1:
            return 1
        elif n in self.steps_dict:
            return self.steps_dict[n]
        if n > 2:
            self.steps_dict[n-1] = self.climbStairs(n-1)
            self.steps_dict[n-2] = self.climbStairs(n-2)
            return self.steps_dict[n-1] + self.steps_dict[n-2]