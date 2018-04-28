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


class ReSolution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_max = right_max = 1
        if root is None:
            return 0
        if root.left:
            left_max = 1 + self.maxDepth(root.left)
        if root.right:
            right_max = 1 + self.maxDepth(root.right)
        return left_max if left_max > right_max else right_max

    def maxDepth2(self, root):
        if root is None:
            return 0
        queue = [root]
        count = 1
        while len(queue) != 0:
            temp_queue = []
            for q in queue:
                if q.left:
                    temp_queue.append(q.left)
                if q.right:
                    temp_queue.append(q.right)
            if len(temp_queue) > 0:
                count += 1
            queue = temp_queue
        return count

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.right = TreeNode(1)
root.left.right.right = TreeNode(1)
solu = ReSolution()
print solu.maxDepth2(root)


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

# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(1)
# root.left.right = TreeNode(1)
# solu = Solution()
# print solu.maxDepth(root)