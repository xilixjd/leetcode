# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        思路1：
        递归
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        if not t.right and t.left:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'
        return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'

    def tree2str2(self, t):
        """
        思路2：
        iter
        看 solution
        :type t: TreeNode
        :rtype: str
        """
        stack = [t]
        visited = []
        s = ""
        while len(stack) != 0:
            tree = stack[-1]
            if tree in visited:
                s += ")"
                stack.pop()
            else:
                visited.append(tree)
                s += "(" + str(tree.val)
                if tree.left is None and tree.right is not None:
                    s += "()"
                if tree.right is not None:
                    stack.append(tree.right)
                if tree.left is not None:
                    stack.append(tree.left)
        return s[1: -1]


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
solu = Solution()
print solu.tree2str2(tree)