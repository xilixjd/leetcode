# -*- coding:utf-8 -*-
'''

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence is None or len(sequence) == 0:
            return False
        root = sequence[len(sequence) - 1]
        i = 0
        while i < len(sequence) - 1:
            if sequence[i] > root:
                break
            i += 1
        j = i
        while j < len(sequence) - 1:
            if sequence[j] < root:
                return False
            j += 1
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i+1:])
        return left and right

solu = Solution()
print solu.VerifySquenceOfBST([5,7,6,9,11,10,8])
