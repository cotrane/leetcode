
class SolutionRecursive:
	# Runtime: O(n*m), Storage: O(1)
	def editDistRec(self, i, j, s1, s2):
		# if first string is empty return second index
		# that is the number of operations
		if i == 0:
			return j
		# if second string is empty return first index
		# that is the number of operations
		if j == 0:
			return i
		# if characters are the same move on to the next
		if s1[i-1] == s2[j-1]:
			return self.editDistRec(i-1, j-1, s1, s2)
		# otherwise add one operation and find the minimum 
		# required ops for the rest
		return 1 + min(
			self.editDistRec(i, j-1, s1, s2), # insert
			self.editDistRec(i-1, j, s1, s2), # remove
			self.editDistRec(i-1, j-1, s1, s2) # replace
		)

	def minDistance(self, word1: str, word2: str) -> int:
		return self.editDistRec(len(word1), len(word2), word1, word2)


class SolutionBottomUp:
	# Runtime O(n*m), Storage: O(n*m)
	def minDistance(self, word1: str, word2: str) -> int:
		l1, l2 = len(word1), len(word2)
		# Initialize
		dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
		for i in range(l1+1):
			dp[i][0] = i
		for j in range(l2+1):
			dp[0][j] = j
		for i in range(1, l1+1, 1):
			for j in range(1, l2+1, 1):
				if word1[i-1] == word2[j-1]:
					dp[i][j] = dp[i-1][j-1]
				else:
					dp[i][j] = 1 + min(
						dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
					)
		return dp[l1][l2]


class SolutionSpaceOptimized:
	# Runtime O(n*m), Storage: O(m)
	def minDistance(self, word1: str, word2: str) -> int:
		l1, l2 = len(word1), len(word2)
		prev = list(range(l2+1))
		for i in range(1, l1+1):
			curr = [i]
			for j in range(1, l2+1):
				if word1[i-1] == word2[j-1]:
					curr.append(prev[j-1])
				else:
					curr.append(1 + min(curr[-1], prev[j], prev[j-1]))
			prev = curr
		return prev[l2]



if __name__ == "__main__":
	text1, text2, output = "horse", "ros", 3
	# text1, text2, output = "intention", "execution", 5
	# text1, text2, output = "cat", "cut", 1
	# text1, text2, output = "saturday", "sunday", 3
	# text1, text2, output = "GEEXSFRGEEKKS", "GEEKSFORGEEKS", 3

	print(text1, text2, output)
	print(SolutionSpaceOptimized().minDistance(text1, text2))


