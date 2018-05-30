# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_dict = {k: 1 for k in wordDict}
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and word_dict.get(s[j: i]) is not None:
                    dp[i] = True
                    break
        return dp[len(s)]

    def wordBreak2(self, s, wordDict):
        '''
        https://leetcode.com/problems/word-break/discuss/130922/python-DFS-98
        :param s:
        :param wordDict:
        :return:
        '''
        start = 0
        stack = [start]
        visited = set()
        while stack:
            start = stack.pop()
            if start in visited:
                continue
            visited.add(start)
            for word in wordDict:
                if s[start:].startswith(word):
                    x = len(word)
                    if x == len(s[start:]):
                        return True
                    stack.append(start + x)
            print stack
        return False

solu = Solution()
print solu.wordBreak2("a" * 21 + "b"
,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])