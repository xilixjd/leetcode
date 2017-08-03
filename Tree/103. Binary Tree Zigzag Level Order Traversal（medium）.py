# -*- coding: utf-8 -*-
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        array = []
        if root is None:
            return array
        queue = [root]
        i = 1
        while len(queue) != 0:
            i += 1
            alist = []
            for q in queue:
                alist.append(q.val)
            if i & 1 == 1:
                alist = alist[::-1]
            array.append(alist)
            queue2 = queue
            queue = []
            for q in queue2:
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        return array

solu = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(2)
root.right.right = TreeNode(11)
print solu.zigzagLevelOrder(root)
