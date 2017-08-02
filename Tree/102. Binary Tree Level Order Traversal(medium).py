# -*- coding: utf-8 -*-

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
import copy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        array = []
        if root is None:
            return array
        queue = [root]
        while len(queue) != 0:
            alist = []
            for i in range(len(queue)):
                alist.append(queue[i].val)
            array.append(alist)
            queue2 = queue
            queue = []
            for i in range(len(queue2)):
                if queue2[i].left:
                    queue.append(queue2[i].left)
                if queue2[i].right:
                    queue.append(queue2[i].right)
        return array

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(32)
root.right.right = TreeNode(11)
solu = Solution()
print solu.levelOrder(root)
