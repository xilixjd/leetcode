'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        leftDepth = 1
        rightDepth = 1
        leftDepth += self.maxDepth(root.left)
        rightDepth += self.maxDepth(root.right)
        return leftDepth if leftDepth > rightDepth else rightDepth

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.right = TreeNode(1)
solu = Solution()
print solu.maxDepth(root)