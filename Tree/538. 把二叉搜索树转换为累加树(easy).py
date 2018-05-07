# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key 
of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sums_dict = {}

        def greater_than_node_sums(root, node):
            if root is None:
                return 0
            sums = 0
            if root.val > node.val:
                sums += root.val
            sums += greater_than_node_sums(root.right, node)
            sums += greater_than_node_sums(root.left, node)
            sums_dict[node] = sums + node.val
            return sums

        def travel_node(root):
            if root is None:
                return
            root.val = sums_dict[root]
            travel_node(root.left)
            travel_node(root.right)

        if root is None:
            return
        temp_node = root
        stack = []
        while temp_node:
            stack.append(temp_node)
            temp_node = temp_node.left
        greater_than_node_sums(root, stack[-1])
        print sums_dict
        last = None
        while len(stack) > 0:
            temp_node = stack[-1]
            print temp_node.val
            if last is not None:
                sums_dict[temp_node] = sums_dict[last] - last.val
            stack.pop()
            last = temp_node
            x = temp_node.right
            while x:
                stack.append(x)
                x = x.left
        travel_node(root)

    def convertBST2(self, root):
        '''
        https://leetcode.com/problems/convert-bst-to-greater-tree/discuss/128179/Python-Simple-Solution(beats-99)
        :param root:
        :return root:
        '''
        self.count = 0

        def inorder(root):
            if root is None:
                return
            inorder(root.right)
            self.count += root.val
            root.val = self.count
            inorder(root.left)

        inorder(root)
        return root

root = TreeNode(1)
# root.left = TreeNode(0)
# root.right = TreeNode(4)
# root.left.left = TreeNode(-2)
# root.right.left = TreeNode(3)

solu = Solution()
solu.convertBST2(None)
# print root