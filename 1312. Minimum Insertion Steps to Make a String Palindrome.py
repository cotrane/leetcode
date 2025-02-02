
class SolutionRecursion:
	# Solve recursively with memoization
	# Runtime: O(N**2), Storage O(1)
    def extendPalindrome(self, i, j, s, cache):
        if (i, j) in cache:
            return cache[(i, j)]

        if s[i] == s[j]:
            length = 2 if i != j else 1
            cache[(i, j)] = length + self.extendPalindrome(i-1, j+1, s, cache)
        else:
            l1 = self.extendPalindrome(i-1, j, s, cache)
            l2 = self.extendPalindrome(i, j+1, s, cache)
            cache[(i, j)] = max(l1, l2)
        return cache[(i, j)]

    def countSubstrings(self, s: str) -> int:
        cache = {}
        for i in range(len(s)):
            self.extendPalindrome(i, i, s, cache)
            self.extendPalindrome(i, i+1, s, cache)
        maxlen = max(cache.values())
        return cnt


class SolutionBottomUp:
    # Find the longest palindrome subsequence and subtract it from 
    # the length of the string
    # Runtime: O(N**2), Storage O(N**2)
    def minInsertions(self, s: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        lss = 0
        # The for loops need to start from opposite ends to test for a 
        # palindrome!
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 2 if i != j else 1
                    if i-1 >= 0:
                        dp[i][j] += dp[i-1][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
                    if i-1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
                lss = max(lss, dp[i][j])
        for ddpp in dp:
            print(ddpp)
        return len(s) - lss



if __name__ == "__main__":
    s, output = "abc", 2
    s, output = "aaa", 0
    s, output = "aabbcc", 4
    s, output = "fdsklf", 3
    s, output = "aba", 0
    s, output = "xabax", 0
    s, output = "xabaxy", 1
    print(s, output)
    print(SolutionBottomUp().minInsertions(s))



