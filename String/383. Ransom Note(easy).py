# -*- coding: utf-8 -*-
'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class ReSolution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m_array = list(magazine)
        for c in ransomNote:
            if c in m_array:
                m_array.remove(c)
            else:
                return False
        return True

re = ReSolution()
print re.canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")


class Solution(object):
    def canConstructMy(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_array = list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine_array:
                magazine_array.remove(ransomNote[i])
            else:
                return False
        return True

solu = Solution()
print solu.canConstructMy('aa', 'ab')