# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def inorder(root, key):
            if root is None:
                return
            if (root.left and root.left.val == key) or (root.right and root.right.val == key):
                return root
            if root.left:
                temp = inorder(root.left, key)
                if temp is not None:
                    return temp
            if root.right:
                temp = inorder(root.right, key)
                if temp is not None:
                    return temp
            return None

        top = TreeNode(-10000000)
        top.right = root
        parent = inorder(root, key)
        stack = []
        temp = root
        last = None
        while temp:
            stack.append(temp)
            temp = temp.left
        while len(stack) > 0 and stack[-1].val != key:
            x = stack.pop()
            last = x
            x = x.right
            while x:
                stack.append(x)
                x = x.left
        if len(stack) == 0:
            return root
        key_node = stack[-1]

        if last is None and parent is None and (key_node.left is None and key_node.right is None):
            return None

        if key_node.left is None and key_node.right is None:
            # key_node = None
            if parent is None:
                return key_node
            if parent.left and parent.left == key_node:
                parent.left = None
            if parent.right and parent.right == key_node:
                parent.right = None
        elif key_node.right and key_node.left:
            if key_node.right.left is None:
                if parent is None:
                    left = top.right.left
                    top.right = key_node.right
                    top.right.left = left
                elif parent.left and parent.left == key_node:
                    left = key_node.left
                    parent.left = key_node.right
                    parent.left.left = left
                elif parent.right and parent.right == key_node:
                    left = key_node.left
                    parent.right = key_node.right
                    parent.right.left = left
                # key_node = key_node.right
            else:
                # last.right = key_node.right
                # key_node = last
                if parent is None:
                    right = key_node.right
                    top.right = key_node.left
                    last.right = right
                elif parent.left and parent.left == key_node:
                    right = key_node.right
                    left = key_node.left
                    last.right = right
                    parent.left = left
                elif parent.right and parent.right == key_node:
                    right = key_node.right
                    left = key_node.left
                    last.right = right
                    parent.right = left
        elif key_node.right is None and key_node.left:
            # key_node = key_node.left
            if parent is None:
                top.right = key_node.left
            elif parent.left and parent.left == key_node:
                parent.left = key_node.left
            elif parent.right and parent.right == key_node:
                parent.right = key_node.left
        elif key_node.left is None and key_node.right:
            # key_node = key_node.right
            if parent is None:
                top.right = key_node.right
            elif parent.left and parent.left == key_node:
                parent.left = key_node.right
            elif parent.right and parent.right == key_node:
                parent.right = key_node.right
        return top.right

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.left = TreeNode(2)

solu = Solution()
print solu.deleteNode(root, 6).val