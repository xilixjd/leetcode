# -*- coding: utf-8 -*-

'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters 
counting from the start of the string. If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
'''

class Solution(object):
    def reverseStr(self, s, k):
        """
        easy 难度
        :type s: str
        :type k: int
        :rtype: str
        """
        array = list(s)
        i = 0
        while i < len(array):
            j = min(i + k - 1, len(array) - 1)
            self.swap(array, i, j)
            i += 2 * k
        return ''.join(array)

    def swap(self, a, i, j):
        a[i:j+1] = a[i:j+1][::-1]

solu = Solution()
print solu.reverseStr('abcdefg', 2)