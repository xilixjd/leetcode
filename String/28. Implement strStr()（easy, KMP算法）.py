# -*- coding: utf-8 -*-
'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
'''


class ReSolution(object):
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1
        if needle == "":
            return 0
        j = 0
        for i in range(len(haystack)):
            while i + j < len(haystack) and haystack[i + j] == needle[j]:
                j += 1
                if j == len(needle):
                    return i
            j = 0
        return -1

re = ReSolution()
print re.strStr("mississippi", "issipi")

class Solution(object):
    def strStr(self, haystack, needle):
        """
        暴力法，太慢了
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)
        if len(needle) > len(haystack):
            return -1
        if needle == "":
            return 0
        for i in range(len(haystack)):
            print i + len(needle) + 1
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def kmp(self, haystack, needle):
        '''
        这篇文章解释还可以介绍了，kmp 算法的过程和 next 数组的计算方法
        http://www.tuicool.com/articles/e2Qbyyf
        :param haystack:
        :param needle:
        :return:
        '''
        next = self.getNext(needle)
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = next[j - 1] + 1
        return (i - j) if j == len(needle) else -1

    def getNext(self, s):
        next = [-1 for i in range(len(s))]
        for i in range(1, len(s)):
            j = next[i - 1]
            # 关键部分 while
            while s[j + 1] != s[i] and j >= 0:
                j = next[j]
            if s[i] == s[j + 1]:
                next[i] = j + 1
            else:
                next[i] = -1
        return next



solu = Solution()
# print solu.kmp("aaa", "aa")