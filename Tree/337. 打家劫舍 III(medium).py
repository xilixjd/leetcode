# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." Besides the root, 
each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        https://leetcode.com/problems/house-robber-iii/discuss/128084/C++-solution-of-the-Step-by-step-tackling-(fun4LeetCode)
        :type root: TreeNode
        :rtype: int
        """
        def robbb(root, root_dict):
            if root is None:
                return 0
            if root_dict.get(root) is not None:
                return root_dict[root]
            sums = root.val
            if root.left:
                sums += robbb(root.left.left, root_dict) + robbb(root.left.right, root_dict)
            if root.right:
                sums += robbb(root.right.left, root_dict) + robbb(root.right.right, root_dict)
            root_dict[root] = max(sums, robbb(root.left, root_dict) + robbb(root.right, root_dict))
            # print root_dict
            return root_dict[root]

        root_dict = {}
        return robbb(root, root_dict)

    def rob1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        sums = root.val
        if root.left:
            sums += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            sums += self.rob(root.right.left) + self.rob(root.right.right)
        return max(sums, self.rob(root.left) + self.rob(root.right))

    def rob2(self, root):
        '''
        rub_sub(root) 返回一个数组 array
        array[0] 代表没有 rub root，
        array[1] 代表 rub 了 root
        :param root:
        :return:
        '''
        def rub_sub(root):
            if root is None:
                return [0, 0]
            left = rub_sub(root.left)
            right = rub_sub(root.right)
            res = [0, 0]
            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = root.val + left[0] + right[0]
            return res

        return max(rub_sub(root))



root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# root.left.left = TreeNode(2)
# root.left.left.left = TreeNode(4)
root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(9)

solu = Solution()
print solu.rob(root)