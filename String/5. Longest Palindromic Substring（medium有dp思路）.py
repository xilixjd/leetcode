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


class ReSolution(object):
    def longestPalindromeMy(self, s):
        '''
        超时
        :param s:
        :return:
        '''
        max_len = 0
        max_palindrome_str = s[0]
        for i in range(len(s)):
            temp_str = s[i]
            for j in range(i + 1, len(s)):
                temp_str += s[j]
                if self.checkPalindrme(temp_str):
                    if len(temp_str) > max_len:
                        max_len = len(temp_str)
                        max_palindrome_str = temp_str
        return max_palindrome_str

    def checkPalindrme(self, s):
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindromeMy2(self, s):
        '''
        二刷看答案得知，还有种方法是动态规划
        这个思路主要是遍历 s
        对每个字母向两边展开，展开结果判断是否回文并选出最大回文字符串
        :param s:
        :return:
        '''
        max_pali_str = s[0]
        max_len = 0
        for i in range(len(s)):
            s1 = self.centerExpand(s, i, i)
            s2 = self.centerExpand(s, i, i + 1)
            if len(s1) > max_len:
                max_pali_str = s1
                max_len = len(s1)
            if len(s2) > max_len:
                max_pali_str = s2
                max_len = len(s2)
        return max_pali_str

    def centerExpand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindromeDynamic(self, s):
        '''
        dp 法，超时
        思路：
        i, j 分别为最长回文的左和右
        s 为字符串
        一般规则：
        dp[i][i] 一定是回文，设为 True
        若 s[i] == s[i + 1] 则 dp[i][i + 1] 一定为回文，设为 True
        dp 遍历情况：
        要判断 dp[i][j] 是否为回文，先判断 dp[i + 1][j - 1] 是否为回文，再判断 s[i] == s[j]
        :param s:
        :return:
        '''
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        max_str = s[0]
        max_len = 1
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_len = 2
                max_str = s[i: i + 2]
        # 这里灵活的是需要以长度为遍历对象
        for length in range(3, len(s) + 1):
            for i in range(len(s) - 2):
                j = length + i - 1
                if j < len(s) and dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    max_len = j - i + 1
                    max_str = s[i: j + 1]
        return max_str

rs = ReSolution()
# print rs.longestPalindromeMy("baafb")
print rs.longestPalindromeDynamic("abcddcba")


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