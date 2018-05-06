# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sums_dict0 = {}

        def find_sum(root):
            if root is None:
                return 0
            if sums_dict0.get(root) is not None:
                return sums_dict0[root]
            sums = 0
            sums += root.val
            sums += find_sum(root.left)
            sums += find_sum(root.right)
            sums_dict0[root] = sums
            return sums_dict0[root]

        def get_all_subtree_sum(root, sums_dict):
            if root is None:
                return
            sums_root = find_sum(root)
            sums_dict[sums_root] = sums_dict.get(sums_root, 0) + 1
            get_all_subtree_sum(root.left, sums_dict)
            get_all_subtree_sum(root.right, sums_dict)

        sums_dict = {}
        get_all_subtree_sum(root, sums_dict)
        max_count = 0
        for key in sums_dict:
            if sums_dict[key] > max_count:
                max_count = sums_dict[key]
        res = []
        for key in sums_dict:
            if sums_dict[key] == max_count:
                res.append(key)
        return res

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

solu = Solution()
print solu.findFrequentTreeSum(root)