# -*- coding: utf-8 -*-

'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
Credits:
'''


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        trans_dict = {}
        j = 0
        for i in range(65, 91):
            trans_dict[j] = chr(i)
            j += 1
        num = n
        s = ""
        while num != 0:
            print (num - 1) % 26
            s += trans_dict[(num - 1) % 26]
            num = (num - 1) / 26

        return s[::-1]

solu = Solution()
print solu.convertToTitle(52)