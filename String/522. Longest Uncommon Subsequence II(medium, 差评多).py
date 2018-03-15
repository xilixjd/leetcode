# -*- coding: utf-8 -*-
'''
Given a list of strings, you need to find the longest uncommon subsequence among them. 
The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
'''


class ReSolution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def is_subsequence(s1, s2):
            if s1 == s2:
                return True
            if len(s1) > len(s2):
                return False
            i = 0
            for c in s2:
                if i < len(s1) and s1[i] == c:
                    i += 1
            return i == len(s1)
        i = j = 0
        res = -1
        while i < len(strs):
            while j < len(strs):
                if i == j:
                    j += 1
                    continue
                if is_subsequence(strs[i], strs[j]):
                    break
                j += 1
            if j == len(strs):
                res = max(res, len(strs[i]))
            i += 1
            j = 0
        return res

re = ReSolution()
print re.findLUSlength(["bca", "bc", "bc"])


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key = len, reverse = True)
        for i, word1 in enumerate(strs):
            if all(not self.subseq(word1, word2) 
                    for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1

    def findLUSlengthLow(self, strs):
        '''
        暴力解法
        '''
        res = -1
        i = j = 0
        # for 循环有个 Bug 全部是 单个 字母时 ["a","b","c","d","e","f","a","b","c","d","e","f"]
        # i == 5 时 if self.subseq(strs[i], strs[j]): 没有 break 
        # for i in range(len(strs)):
        #     for j in range(len(strs)):
        #         print i, j
        #         if i == j:
        #             continue
        #         # print strs[i], strs[j]
        #         if self.subseq(strs[i], strs[j]):
        #             break
        #     if j == len(strs) - 1:
        #         res = max(res, len(strs[i]))
        while i < len(strs):
            while j < len(strs):
                if i == j:
                    j += 1
                    continue
                if self.subseq(strs[i], strs[j]):
                    break
                j += 1
            if j == len(strs):
                res = max(res, len(strs[i]))
                
            j = 0
            i += 1
        return res

    def wh(self, num):
        i = j = 0
        while i < num:
            while j < num:
                print i, j
                j += 1
            j = 0
            i += 1

    def subseq(self, w1, w2):
        #True iff word1 is a subsequence of word2.
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return i == len(w1)
                

solu = Solution()
print solu.findLUSlengthLow(["abc","accbdc","abc"])
# solu.wh(3)