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


class ReSolution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent_count = 0
        prev_late_flag = False
        late_start = late_end = -1
        for i in range(len(s)):
            if s[i] == 'A':
                absent_count += 1
                if absent_count > 1:
                    return False
                prev_late_flag = False
            if s[i] == 'L':
                if prev_late_flag:
                    late_end = i
                    if late_end - late_start >= 2:
                        return False
                else:
                    late_start = i
                    prev_late_flag = True
            if s[i] == 'P':
                prev_late_flag = False
            i += 1
        return True

re = ReSolution()
print re.checkRecord("PPALLPLL")

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
