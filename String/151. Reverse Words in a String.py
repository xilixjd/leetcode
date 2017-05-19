# -*- coding: utf-8 -*-

'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''


class Solution(object):
    def reverseWordsMy(self, s):
        """
        91% !!
        :type s: str
        :rtype: str
        """
        array = s.split(' ')
        deleteArray = []
        for i in range(len(array)):
            if array[i].isspace() or len(array[i]) == 0:
                deleteArray.append(i)
        for i in range(len(deleteArray))[::-1]:
            array.pop(deleteArray[i])
        array.reverse()
        return ' '.join(array)

solu = Solution()
print solu.reverseWordsMy(' ')