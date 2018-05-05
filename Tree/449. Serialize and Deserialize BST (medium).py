# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same 
or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def inorder(root, array):
            if root is None:
                return
            inorder(root.left, array)
            array.append(str(root.val))
            inorder(root.right, array)

        def preorder(root, array):
            if root is None:
                return
            array.append(str(root.val))
            preorder(root.left, array)
            preorder(root.right, array)

        array1 = []
        array2 = []
        preorder(root, array1)
        inorder(root, array2)
        array1_str = ",".join(array1)
        array2_str = ",".join(array2)
        return array1_str + "." + array2_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def construct_tree(preorder, prel, prer, inorder, inl, inr, inorder_map):
            if prel > prer or inl > inr:
                return
            root = TreeNode(int(preorder[prel]))
            in_index = inorder_map[preorder[prel]]
            root.left = construct_tree(preorder, prel + 1, prel + in_index - inl, inorder, inl, in_index - 1, inorder_map)
            root.right = construct_tree(preorder, prel + in_index - inl + 1, prer, inorder, in_index + 1, inr, inorder_map)
            return root

        array = data.split(".")
        preorder = array[0].split(",")
        inorder = array[1].split(",")
        inorder_map = {}
        for i in range(len(inorder)):
            if inorder[i] == "":
                return
            inorder_map[inorder[i]] = i
        root = construct_tree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inorder_map)
        return root

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
# root.left.right = TreeNode(6)
root.right.left = TreeNode(4)
root.right.right = TreeNode(9)

codec = Codec()
print codec.serialize(None)
print codec.deserialize(codec.serialize(None))