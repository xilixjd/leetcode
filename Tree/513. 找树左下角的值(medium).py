# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        res = []
        while len(queue) > 0:
            res.append([q.val for q in queue])
            temp_queue = []
            for q in queue:
                if q.left:
                    temp_queue.append(q.left)
                if q.right:
                    temp_queue.append(q.right)
            queue = temp_queue

        return res[-1][0]

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

solu = Solution()
print solu.findBottomLeftValue(root)