# -*- coding: utf-8 -*-
'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

class ReSolution(object):
    def compareVersion(self, version1, version2):
        """
        考虑 1.1.0 和 1.1 都是一样的
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_array = version1.split(".")
        v2_array = version2.split(".")
        i = j = 0
        while i < len(v1_array) and j < len(v2_array):
            if int(v1_array[i]) > int(v2_array[j]):
                return 1
            elif int(v1_array[i]) < int(v2_array[j]):
                return -1
            else:
                i += 1
                j += 1
        for x1 in v1_array[i:]:
            if int(x1) > 0:
                return 1
        for x2 in v2_array[j:]:
            if int(x2) > 0:
                return -1
        return 0

re = ReSolution()
print re.compareVersion('1.1.0', '1.1')

class Solution(object):
    def compareVersionMy(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        array1 = version1.split('.')
        array2 = version2.split('.')
        i = j = 0
        while i < len(array1) and j < len(array2):
            if int(array1[i]) > int(array2[j]):
                return 1
            elif int(array1[i]) < int(array2[j]):
                return -1
            else:
                i += 1
                j += 1
        for a1 in array1[i:]:
            if int(a1) > 0:
                return 1
        for a2 in array2[j:]:
            if int(a2) > 0:
                return -1
        return 0

solu = Solution()
print solu.compareVersionMy('1', '1.1')