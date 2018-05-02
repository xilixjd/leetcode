# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the 
lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, 
since a node can be a descendant of itself according to the LCA definition.
'''


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
        mid = root
        if p.val < q.val:
            while True:
                if p.val < mid.val and q.val < mid.val:
                    mid = mid.left
                if p.val > mid.val and q.val > mid.val:
                    mid = mid.right
                if p.val < mid.val < q.val:
                    return mid
                if p.val == mid.val or q.val == mid.val:
                    return mid
        elif p.val > q.val:
            while True:
                if p.val < mid.val and q.val < mid.val:
                    mid = mid.left
                if p.val > mid.val and q.val > mid.val:
                    mid = mid.right
                if q.val < mid.val < p.val:
                    return mid
                if p.val == mid.val or q.val == mid.val:
                    return mid
        else:
            return p

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.left = TreeNode(9)

root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
solu = Solution()
print solu.lowestCommonAncestor(root, root.left.right.left, root.left.right.right).val