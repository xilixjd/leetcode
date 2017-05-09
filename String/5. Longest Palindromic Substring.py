# -*- coding: utf-8 -*-
'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''


class Solution(object):
    def longestPalindromeMy(self, s):
        """
        超时
        :type s: str
        :rtype: str
        """
        max_len = 0
        if len(s) == 0:
            return
        longest_pal = "{}".format(s[0])
        for i in range(len(s)):
            temp_str = "{}".format(s[i])
            for j in range(i+1, len(s)):
                temp_str += s[j]
                if self.checkPalindrome(temp_str):
                    if max_len < len(temp_str):
                        max_len = len(temp_str)
                        longest_pal = temp_str
        return longest_pal

    def longestPalindromeMy2(self, s):
        '''
        仍旧超时，但比上一个好点
        :param s:
        :return:
        '''
        max_len = 0
        if len(s) == 0:
            return
        array = [s[0]]
        longest_pal = "{}".format(s[0])
        arr_dict = {}
        arr_dict[s[0]] = [0]
        for i in range(1, len(s)):
            if arr_dict.get(s[i]) is None:
                arr_dict[s[i]] = [i]
                array.append(s[i])
            else:
                array.append(s[i])
                for j in arr_dict[s[i]]:
                    temp_str = ''.join(array[j:])
                    if self.checkPalindrome(temp_str):
                        if max_len < len(temp_str):
                            max_len = len(temp_str)
                            longest_pal = temp_str
                arr_dict[s[i]].append(i)
        return longest_pal

    def checkPalindrome(self, s):
        mid = (len(s) - 1) / 2
        fl = len(s) % 2
        if fl:
            return s[:mid] == s[mid+1:][::-1]
        else:
            return s[:mid+1] == s[mid+1:][::-1]

    def longestPalindromeFast(self, s):
        '''
        网上思路：
        遍历 s ，从 s[i] 开始向两边展开，如果有不相等的，立马 break 计算长度
        :param s:
        :return:
        '''
        if len(s) == 0:
            return
        longest_str = s[0]
        for i in range(len(s) - 1):
            s1 = self.expendFromCenter(s, i, i)
            print 's1', s1
            if len(s1) > len(longest_str):
                longest_str = s1
            s2 = self.expendFromCenter(s, i, i + 1)
            print 's2', s2
            if len(s2) > len(longest_str):
                longest_str = s2

        return longest_str


    def expendFromCenter(self, s, l, r):
        OddFlag = False
        if l != r:
            OddFlag = True
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # if OddFlag:
        #     return s[l+1:r-l]
        # else:
        return s[l+1:r]

solu = Solution()
print solu.longestPalindromeFast('abccba')