# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def inorder(root, array):
            if root is None:
                return
            inorder(root.left, array)
            array.append(root)
            inorder(root.right, array)

        self.array = []
        self.pointer = 0
        inorder(root, self.array)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointer != len(self.array)

    def next(self):
        """
        :rtype: int
        """
        the_next = self.array[self.pointer]
        self.pointer += 1
        return the_next.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
bst = BSTIterator(root)
i, v = BSTIterator(root), []
while i.hasNext():
    v.append(i.next())
print v