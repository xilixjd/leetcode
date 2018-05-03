# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''
import copy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def find_path(root, array, res):
            if root is None:
                return
            array.append(str(root.val))
            if root.left is None and root.right is None:
                res.append(copy.copy(array))
            find_path(root.left, array, res)
            find_path(root.right, array, res)
            array.pop()

        res = []
        find_path(root, [], res)
        r = []
        for rr in res:
            r.append("->".join(rr))
        return r


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

# root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(9)

solu = Solution()
print solu.binaryTreePaths(root)