# -*- coding: utf-8 -*-

'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
'''


class Solution(object):
    def groupAnagramsMy(self, strs):
        """
        9%
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        array = []
        for i in range(len(strs)):
            temp_array = list(strs[i])
            temp_array.sort()
            array.append("".join(temp_array))
        i = 0
        for j in range(len(array)):
            if str_dict.get(array[j]) is None:
                str_dict[array[j]] = [j]
            else:
                str_dict[array[j]].append(j)
        # print str_dict
        result = []
        for k in str_dict:
            temp_array = []
            for i in range(len(str_dict[k])):
                temp_array.append(strs[str_dict[k][i]])
            result.append(temp_array)
        return result


    def isAnagrams(self, str1, str2):
        for s in str2:
            if s not in str1:
                return False

        return True

solu = Solution()
print solu.groupAnagramsMy(["eat", "tea", "tan", "ate", "nat", "bat"])