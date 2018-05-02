# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the 
lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. 
Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''
import copy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def get_path(root, p, q, array, res):
            if root is None:
                return
            array.append(root)
            if p == root or q == root:
                res.append(copy.copy(array))
            get_path(root.left, p, q, array, res)
            get_path(root.right, p, q, array, res)
            array.pop()

        res = []
        get_path(root, p, q, [], res)
        print [[x.val for x in r] for r in res]
        p1 = res[0]
        p2 = res[1]
        i = j = 0
        node = None
        while i < len(p1) and j < len(p2):
            if p1[i] == p2[j]:
                node = p1[i]
            i += 1
            j += 1
        return node

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

# root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(9)
#
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
solu = Solution()
print solu.lowestCommonAncestor(root, root.left.right, root.right.left).val