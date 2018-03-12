# -*- coding: utf-8 -*-
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class ReSolution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_array = list(s)
        record_array = []
        for i in range(len(s_array)):
            if s[i] in vowels:
                record_array.append(i)
        i = 0
        j = len(record_array) - 1
        while i < j:
            s_array[record_array[i]], s_array[record_array[j]] = s_array[record_array[j]], s_array[record_array[i]]
            i += 1
            j -= 1
        return ''.join(s_array)

re = ReSolution()
print re.reverseVowels("leetcode")

import copy
class Solution(object):
    def reverseVowelsMy(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = list(s)
        copy_array = copy.deepcopy(array)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_array = []
        for i in range(len(array)):
            if array[i] in vowels:
                vowel_array.append(i)
        copy_v = copy.deepcopy(vowel_array)
        vowel_array.reverse()
        for i in range(len(copy_v)):
            array[copy_v[i]] = copy_array[vowel_array[i]]
        return ''.join(array)

solu = Solution()
print solu.reverseVowelsMy('aA')