# -*- coding: utf-8 -*-

'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
'''

class Solution(object):
    def detectCapitalUseMy(self, word):
        """
        :type word: str
        :rtype: bool
        """
        first_word = word[0]
        if len(word) > 1:
            if first_word.isupper():
                upper_flag = True if word[1].isupper() else False
                if upper_flag:
                    for i in range(1, len(word)):
                        if not word[i].isupper():
                            return False
                else:
                    for i in range(1, len(word)):
                        if word[i].isupper():
                            return False
            else:
                for i in range(1, len(word)):
                    if word[i].isupper():
                        return False
        return True

solu = Solution()
print solu.detectCapitalUseMy('abC')