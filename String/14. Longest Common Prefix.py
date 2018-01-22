# -*- coding: utf-8 -*-
'''
Write a function to find the longest common prefix string amongst an array of strings.

'''


class ReSolution(object):
    def longestCommonPrefixMy(self, strs):
        '''
        思路：
        从数组的第一个字符串开始作为 compare，遍历之后的数组
        若 compare 在之后的字符串中 index 不为 0，则从 compare 最后去掉一个字符
        :param strs:
        :return:
        '''
        if len(strs) == 0:
            return ""
        compare_str = strs[0]
        i = 1
        while i < len(strs):
            if strs[i].find(compare_str) != 0:
                compare_str = compare_str[:len(compare_str) - 1]
            else:
                i += 1
            if len(compare_str) == 0:
                break
        return compare_str


rs = ReSolution()
print rs.longestCommonPrefixMy(['c', 'acc', 'ccc'])
print rs.longestCommonPrefixMy([''])

class Solution(object):
    def longestCommonPrefixMy(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        compare_str = strs[0]
        for i in range(1, len(strs)):
            compare_str = self.compare_remainder_str(compare_str, strs[i])
        return compare_str


    def compare_remainder_str(self, orig_str, tar_str):
        if tar_str == "" or orig_str == "":
            return ""
        temp_str = tar_str[0]
        i = 0
        while temp_str == orig_str[:i + 1]:
            i += 1
            if len(tar_str) - 1 < i:
                break
            temp_str += tar_str[i]
        return temp_str[:i]

    def longestCommonPrefixFast(self, strs):
        '''
        pre 从后往前判断居然要快一些
        我的方法有些画蛇添足了
        :param strs:
        :return:
        '''
        if len(strs) == 0:
            return ""
        pre = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(pre) != 0:
                pre = pre[:len(pre)-1]
            i += 1
        return pre

solu = Solution()
# print solu.longestCommonPrefixMy(['aa', 'aab', 'aabd'])
print solu.longestCommonPrefixFast(['aa', 'aab'])