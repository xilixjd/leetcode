# -*- coding: utf-8 -*-

'''
Given two words word1 and word2, find the minimum number of steps required to make word1
and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
'''

class ReSolution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[len(word1)][len(word2)]

re = ReSolution()
print re.minDistance('eat', 'sea')

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        思路： dp[i][j] 看成 是 word1(0, i) 变成 word2(0, j) 所需要的步骤
        初始情况：dp[0][j] 等于 从 0 到 j
        dp[i][0] 等于从 0 到 i
        方程：word1[i] == word2[j] 则 dp[i][j] = dp[i-1][j-1]
        不等于 则有 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        """
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[i][j]

solu = Solution()
print solu.minDistance('eat', 'atd')
