
class SolutionRecursion:
	# Solve recursively with memoization
	# Runtime: O(N**2), Storage O(1)
    def extendPalindrome(self, i, j, s):
        cnt=0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            cnt += 1
            i -= 1
            j += 1
        return cnt

    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            cnt += self.extendPalindrome(i, i, s)
            cnt += self.extendPalindrome(i, i+1, s)
        return cnt


class SolutionBottomUp:
    # Solve differently
    # Runtime: O(N**2), Storage O(N**2)
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        res = 0
        num_pali = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        # The for loops need to start from opposite ends to test for a 
        # palindrome!
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if i == j else 2
                    num_pali[i][j] = 1
                    if i - 1 >= 0:
                        dp[i][j] += dp[i-1][j+1]
                    if i != j:
                        num_pali[i][j] += num_pali[i-1][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
                res = max(res, dp[i][j])
        for ddpp in num_pali:
            print(ddpp)
        out = 0
        for i in range(len(s)):
            for j in range(i, min(i+3, len(s)), 1):
                out += num_pali[i][j]
        return out



if __name__ == "__main__":
    s, output = "abc", 3
    s, output = "aaa", 6
    s, output = "aabbcc", 9
    # s, output = "aaaaa", 15
    # s, output = "fdsklf", 6
    # s, output = "aba", 4
    # s, output = "xabax", 7
    s, output = "xabaxy", 8
    print(s, output)
    print(SolutionRecursion().countSubstrings(s))



