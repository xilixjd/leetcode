# -*- coding: utf-8 -*-
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstringMy(self, s):
        """
        无法通过最后一个测试用例，超时
        :type s: str
        :rtype: int
        """
        max_len = 0
        for i in range(len(s)):
            temp_array = [s[i]]
            for j in range(i + 1, len(s)):
                if s[j] not in temp_array:
                    temp_array.append(s[j])
                else:
                    break
            max_len = max(max_len, len(temp_array))
        return max_len

    def lengthOfLongestSubstringMy2(self, s):
        '''
        个人思路：s = "abcabcbb"
        建立一个 数组 a = []
        遍历 s ,有不同就向数组添加元素，到第二个 'a' 时，a = ['a', 'b', 'c']
        有重复，删掉数组中重复元素之前的所有重复元素并在数组后添加当前元素 a = ['b', 'c', 'a']
        击败 7%
        效率差
        :param s:
        :return:
        '''
        max_len = 0
        temp_dict = {}
        temp_array = []
        for i in range(len(s)):
            if temp_dict.get(s[i]) is None:
                temp_array.append(s[i])
                temp_dict[s[i]] = len(temp_array) - 1
                print "if", temp_dict
                print temp_array
                max_len = max(len(temp_array), max_len)
            else:
                pos = temp_dict.get(s[i])
                pos_temp = pos
                print "else", temp_dict
                print temp_array
                while pos_temp >= 0 and len(temp_array) != 0:
                    del temp_dict[temp_array[0]]
                    temp_array.pop(0)
                    pos_temp -= 1
                for x in range(pos + 1):
                    for key in temp_dict:
                        temp_dict[key] -= 1
                temp_array.append(s[i])
                temp_dict[s[i]] = len(temp_array) - 1
                print temp_dict
                print temp_array
                max_len = max(len(temp_array), max_len)
        return max_len

    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        tem_dict = {}
        max_len = 0
        j = 0
        for i in range(len(s)):
            if tem_dict.get(s[i]) is not None:
                j = max(j, tem_dict.get(s[i]) + 1)
            tem_dict[s[i]] = i
            max_len = max(max_len, i - j + 1)
        return max_len




solu = Solution()
print solu.lengthOfLongestSubstring("ggububgvfk")