# -*- coding: utf-8 -*-
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ReSolution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sym_trees(root1, root2):
            if root1 is None:
                return root2 is None
            if root2 is None:
                return root1 is None
            if root1.val != root2.val:
                return False
            return sym_trees(root1.left, root2.right) and sym_trees(root1.right, root2.left)

        if root is None:
            return True
        return sym_trees(root.left, root.right)

solu = ReSolution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
print solu.isSymmetric(root)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        deque = [root.left, root.right]
        preNode = None
        postNode = None
        while len(deque) != 0:
            preNode = deque[0]
            deque.pop(0)
            postNode = deque[len(deque) - 1]
            deque.pop()
            if preNode is None and postNode is None:
                continue
            if preNode is None or postNode is None:
                return False
            if preNode.val != postNode.val:
                return False
            deque.insert(0, preNode.right)
            deque.insert(0, preNode.left)
            deque.append(postNode.left)
            deque.append(postNode.right)
        return True

# solu = Solution()
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(2)
# root.right = TreeNode(2)
# root.right.right = TreeNode(2)
# print solu.isSymmetric(root)
