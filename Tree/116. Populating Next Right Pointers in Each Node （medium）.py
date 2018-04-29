# -*- coding:utf-8 -*-

'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class ReSolution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        path = [root]
        while len(path) != 0:
            for i in range(len(path)):
                if path[i] is None:
                    return
                if i == len(path) - 1:
                    path[i].next = None
                else:
                    path[i].next = path[i + 1]
            temp_array = []
            for p in path:
                if p.left:
                    temp_array.append(p.left)
                if p.right:
                    temp_array.append(p.right)
            path = temp_array


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        path = [root]
        if root is None:
            return None
        self.findPath(path)

    def findPath(self, path):
        while len(path) != 0:
            self.connectSameLevel(path)
            path2 = path
            path = []
            for p in path2:
                if p.left:
                    path.append(p.left)
                if p.right:
                    path.append(p.right)

    def connectSameLevel(self, path):
        for i in range(len(path)):
            if i + 1 >= len(path):
                path[i].next = None
            else:
                path[i].next = path[i + 1]

root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
solu = Solution()
solu.connect(root)
print root.right.next