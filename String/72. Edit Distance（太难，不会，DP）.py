# -*- coding: utf-8 -*-
'''
Given two words word1 and word2,
find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''


class Solution(object):
    def minDistanceMy(self, word1, word2):
        """
        如果word1[i-1]等于word2[j-1]，则表明该位置不需要操作，即d[i, j] = d[i-1, j-1]；
        如果word1[i-1]不等于word2[j-1]，则可能需要删除或添加或替换字符。
        如果需要删除或添加字符（删除和添加实为相反操作，这里只考虑删除吧）。
        可以选择删除word1[i-1]，这样d[i, j]就是word1的前i-1位和word2的前j位的距离再加1步删除操作，
        即d[i, j] = d[i-1, j] + 1。如果删除word1[j-1]，则d[i, j] = d[i, j-1] + 1。
        当然，如果替换，则d[i, j] = d[i-1, j-1] + 1。因此，d[i, j] = min(d[i-1, j], d[i, j-1], d[i-1, j-1]) + 1
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        p = [[0 for i in range(len2)] for j in range(len1)]
        if len(p[0]) == 1 and len(p) == 1:
            return 0
        for i in range(len1):
            p[i][0] = i
        for i in range(len2):
            p[0][i] = i
        # print p
        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i - 1] == word2[j - 1]:
                    p[i][j] = p[i - 1][j - 1]
                else:
                    p[i][j] = min(p[i - 1][j], p[i - 1][j - 1], p[i][j - 1]) + 1
        return p[len1-1][len2-1]


solu = Solution()
print solu.minDistanceMy("", "a")