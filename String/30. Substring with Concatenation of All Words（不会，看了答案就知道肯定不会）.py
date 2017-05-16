# -*- coding: utf-8 -*-
'''
You are given a string, s, and a list of words, words,
that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''
from copy import deepcopy

class Solution(object):
    def findSubstringMy(self, s, words):
        """
        超时。。。。。
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        sentence = []
        sentence = self.getSentence(words, sentence)
        sentence = set(sentence)
        sentence = list(sentence)
        result = []
        for sen in sentence:
            index = s.find(sen)
            while index != -1:
                result.append(index)
                index = s[index + 1:].find(sen)
                if index != -1:
                    index += 1
            # if index != -1:
            #     result.append(index)
        return result

    def getSentence(self, words, result):
        '''
        :param words:
        :param array:
        :return:
        排列组合
        '''
        if len(words) > 1:
            elmentCur = words.pop(0)
            self.getSentence(words, result)
            resultLen = len(result)
            for j in range(resultLen):
                p = result.pop(0)
                for i in range(len(p) + 1):
                    r = deepcopy(p)
                    r.insert(i, elmentCur)
                    result.append(r)
        else:
            result.append([words[0]])
        return ["".join(r) for r in result]

solu = Solution()
words = ["aa","aa", 'aa']
array = []
print solu.findSubstringMy("aaaaaa", words)