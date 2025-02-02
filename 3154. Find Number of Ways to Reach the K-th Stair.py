class Solution:
    d = {}
    def waysToReachStair(self, k: int) -> int:
        def climbStairs(k, i, jump, down):
            success = 1 if i == k else 0
            if i < k+2:
                if i > 0 and down:
                    c = (k, i-1, jump, False)
                    if c in self.d:
                        success += self.d[c]
                    else:
                        s1 = climbStairs(*c)
                        self.d[c] = s1
                        success += s1
                c = (k, i + 2**jump, jump+1, True)
                if c in self.d:
                    success += self.d[c]
                else:
                    s2 = climbStairs(*c)
                    self.d[c] = s2
                    success += s2
            return success
        
        return climbStairs(k, 1, 0, True)