# -*- coding: utf-8 -*-

'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''

class ReSolution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words_array = s.split(" ")
        print words_array
        array = []
        for words in words_array:
            if not (words.isspace() or len(words) == 0):
                array.append(words)
        array.reverse()
        return ' '.join(array)

re = ReSolution()
print re.reverseWords("the sky  is blue")


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