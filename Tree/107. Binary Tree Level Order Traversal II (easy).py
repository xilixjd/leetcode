'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
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
            for q in queue:
                alist.append(q.val)
            array.append(alist)
            queue2 = queue
            queue = []
            for q in queue2:
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        return array[::-1]