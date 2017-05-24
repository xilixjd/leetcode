# -*- coding: utf-8 -*-

'''
You are given a string representing an attendance record for a student. 
The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) 
or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
'''
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = l = 0
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
                if a > 1:
                    return False
                l = 0
            elif s[i] == 'L':
                l += 1
                if l > 2:
                    return False
            else:
                l = 0
        return True

solu = Solution()
print solu.checkRecord('PPALLLP')
