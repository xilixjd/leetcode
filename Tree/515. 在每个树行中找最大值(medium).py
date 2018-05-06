# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
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

        answer = [max(r) for r in res]
        return answer