from typing import List


class Solution:
    # Backtracking - Bottom Up
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * (l+1)
        # If we are at the end of the string we have succeeded
        dp[l] = True
        # Iterate over each character in s
        for i in range(l - 1, -1 , -1):
            # and check if any word starts with that character
            for w in wordDict:
                # If so, check that it covers all characters leading
                # to the previous matched word (or the end)
                if (i + len(w)) <= l and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                # if a word matched we can break the search
                if dp[i]:
                    break
        return dp[0]



if __name__ == "__main__":
    s, wordDict, output = "leetcode", ["leet","code"], True
    s, wordDict, output = "leetcode", ["leet","leet"], False
    s, wordDict, output = "applepenapple", ["apple","pen"], True
    s, wordDict, output = "catsandog", ["cats","dog","sand","and","cat"], False
    s, wordDict, output = "bb", ["a","b","bbb","bbbb"], True
    s, wordDict, output = "a", ["b"], False
    s, wordDict, output = "abcd", ["a","abc","b","cd"], True

    print(s, wordDict, output)
    print(Solution().wordBreak(s, wordDict))