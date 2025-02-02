
class SolutionRecursive:
    # Runtime O(l1*l2), Space: O(l1*l2)
    def editDist(self, i, j, s1, s2):
        if i == 0:
            print(s2[:j])
            return sum(ord(s2[jj]) for jj in range(j))
        if j == 0:
            print(s1[:i])
            return sum(ord(s1[ii]) for ii in range(i))
        if s1[i-1] == s2[j-1]:
            out = self.editDist(i-1, j-1, s1, s2)
        else:
            print(s1[i-1], s2[j-1], ord(s1[i-1]), ord(s2[j-1]))
            out = min(
                ord(s1[i-1]) + self.editDist(i-1, j, s1, s2),
                ord(s2[j-1]) + self.editDist(i, j-1, s1, s2)
            )
        return out

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        return self.editDist(len(s1), len(s2), s1, s2)


class SolutionBottomUp:
    # Runtime O(l1*l2), Space: O(l1*l2)
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, l2+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, l1+1, 1):
            for j in range(1, l2+1, 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        ord(s2[j-1]) + dp[i][j-1], 
                        ord(s1[i-1]) + dp[i-1][j]
                    )
        for d in dp:
            print(d)
        return dp[l1][l2]


class SolutionSpaceOptimized:
    # Runtime O(l1*l2), Space: O(l2)
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)

        # Initialize previous row with cumulative ASCII sums of s2
        prev = [0] * (l2 + 1)
        for j in range(1, l2 + 1):
            prev[j] = prev[j-1] + ord(s2[j-1])

        for i in range(1, l1+1):
            # Initialize current row with ASCII sum of current char from s1
            curr = [sum(ord(s1[k]) for k in range(i))]
            for j in range(1, l2+1):
                if s1[i-1] == s2[j-1]:
                    curr.append(prev[j-1])
                else:
                    curr.append(min(
                        prev[j] + ord(s1[i-1]), 
                        curr[-1] + ord(s2[j-1])
                    ))
            prev = curr
        # print(prev)
        return prev[l2]


if __name__ == "__main__":
    # s1, s2, output = "sea", "eat", 231
    s1, s2, output = "delete", "leet", 403

    print(s1, s2, output)
    print(SolutionSpaceOptimized().minimumDeleteSum(s1, s2))