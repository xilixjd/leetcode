# -*- coding:utf-8 -*-
'''

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
class Solution:
    def Permutation(self, ss):
        # write code here
        res = []
        if ss is None or len(ss) == 0:
            return []
        array = list(ss)
        self.PermutationPrint(array, 0, res)
        return res

    def PermutationPrint(self, ss, start, res):
        if start == len(ss):
            if ''.join(ss) not in res:
                res.append(''.join(ss))
        for i in range(start, len(ss)):
            ss[start], ss[i] = ss[i], ss[start]
            self.PermutationPrint(ss, start + 1, res)
            ss[start], ss[i] = ss[i], ss[start]

solu = Solution()
print solu.Permutation('abc')