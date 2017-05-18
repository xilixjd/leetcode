# -*- coding: utf-8 -*-
'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        '''
        http://blog.csdn.net/hellochenlu/article/details/50883633
        f[i][j] 看成 s1 的前 i 个字符串与 s2 的前 j 个字符串所组成的组合符不符合 interleaving
        f[i][j] 只有两种情况算出，第一种：选取的 s2 的字符，因此只判断 f[i][j-1] and s2[j-1] == s3[i+j-1]
         第二种：选取 s1 的字符，因此只判断 f[i-1][j] and s1[i-1] == s3[i+j-1]
        :param s1:
        :param s2:
        :param s3:
        :return:
        '''
        if len(s1) + len(s2) != len(s3):
            return False
        f = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        f[0][0] = True
        for i in range(1, len(s1) + 1):
            f[i][0] = f[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, len(s2) + 1):
            f[0][i] = f[0][i-1] and s2[i-1] == s3[i-1]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                f[i][j] = f[i][j-1] and s2[j-1] == s3[i+j-1] or f[i-1][j] and s1[i-1] == s3[i+j-1]
        return f[len(s1)][len(s2)]

    def isInterleaveRecur(self, s1, s2, s3):
        """
        会超时
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if len(s3) == 0:
            return len(s1) == 0 and len(s3) == 0
        if s1[0] == s3[0] and s2[0] != s3[0]:
            return self.isInterleaveRecur(s1[1:], s2, s3[1:])
        if s1[0] != s3[0] and s2[0] == s3[0]:
            return self.isInterleaveRecur(s1, s2[1:], s3[1:])
        if s1[0] == s3[0] and s2[0] == s3[0]:
            return self.isInterleaveRecur(s1[1:], s2, s3[1:]) or self.isInterleaveRecur(s1, s2[1:], s3[1:])
        else:
            return False

solu = Solution()
print solu.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
