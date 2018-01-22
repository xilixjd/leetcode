# -*- coding: utf-8 -*-
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class ReSolution(object):
    def lengthOfLongestSubstringMy(self, s):
        '''
        二刷
        最后一个例子通过不了，思路：
        'dvdf'
        初始化一个 dict 去重
        遍历字符串，若没重复，则添加到 dict, i += 1
        若重复，则 dict 重建并添加重复的 i 的 index + 1 的字母到 dict，i 回到 index + 2 的位置

        缺点：若不重复的过多，空间太大，且回退的步骤太多

        按我写过的思路再来一遍
        :param s:
        :return:
        '''
        filter_dict = {}
        max_len = current_len = 0
        i = j = 0
        # flag = True
        while i < len(s):
            # print filter_dict
            if filter_dict.get(s[i]) is None:
                # if not flag:
                #     j = i
                current_len += 1
                filter_dict[s[i]] = i
                # flag = False
            else:
                # 最后一个例子超时
                current_len = 1
                temp_dict = {}
                if i < len(s) - 1:
                    temp_dict[s[filter_dict[s[i]] + 1]] = filter_dict[s[i]] + 1
                i = filter_dict[s[i]] + 2
                filter_dict = temp_dict
                # index = filter_dict[s[i]]
                # current_len = i - index
                # flag = True
                # print filter_dict, j, index
                # for k in range(j, index + 1):
                #     del filter_dict[s[k]]
                # filter_dict[s[i]] = i
            i += 1
            max_len = max(max_len, current_len)
        return max_len

    def lengthOfLongestSubstringMy2(self, s):
        '''
        重复之前个人思路，改良版击败 20%
        :param s:
        :return:
        '''
        array = []
        max_len = 0
        for i in range(len(s)):
            # print array
            if s[i] not in array:
                array.append(s[i])
            else:
                index = array.index(s[i])
                # print array, index, i
                array.append(s[i])
                for j in range(index + 1):
                    array.pop(0)
            max_len = max(max_len, len(array))
        return max_len


rs = ReSolution()
# print rs.lengthOfLongestSubstringMy("abcabcbb")
print rs.lengthOfLongestSubstringMy2("dvdf")


class Solution(object):
    def lengthOfLongestSubstringMy(self, s):
        """
        暴力法
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
# print solu.lengthOfLongestSubstring("ggububgvfk")