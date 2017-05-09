# -*- coding: utf-8 -*-

'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        用队列的先进先出方法
        高端思路
        :type digits: str
        :rtype: List[str]
        """
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = ['']
        for i in range(len(digits)):
            x = int(digits[i])
            while len(ans[0]) == i:
                t = ans.pop(0)
                for s in mapping[x]:
                    ans.append(t + s)
        return ans

    def letterCombinationsAnother(self, digits):
        '''
        3 个 for 循环
        :param digits:
        :return:
        '''
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = ['']
        for i in range(len(digits)):
            tempres = []
            chars = mapping[int(digits[i])]
            for c in chars:
                for j in ans:
                    tempres.append(j+c)
            ans = tempres
        return ans

solu = Solution()
print solu.letterCombinationsAnother('23433')
