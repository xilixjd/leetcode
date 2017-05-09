# -*- coding: utf-8 -*-
'''
Write a function to find the longest common prefix string amongst an array of strings.

'''


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
        pre = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(pre) != 0:
                pre = pre[:len(pre)-1]
            i += 1
        return pre

solu = Solution()
print solu.longestCommonPrefixMy(['aa', 'aab'])
print solu.longestCommonPrefixFast(['aa', 'aab'])