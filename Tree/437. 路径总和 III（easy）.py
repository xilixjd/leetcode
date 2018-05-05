# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
import copy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.count = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def sum_array(array):
            sums = 0
            for a in array:
                sums += a
            return sums

        def find_path(root, array, res):
            if root is None:
                return
            array.append(root.val)
            if sum_array(array) == sum:
                res.append(copy.copy(array))
            find_path(root.left, array, res)
            find_path(root.right, array, res)
            array.pop()

        def find_path_in_tree(root, res):
            if root is None:
                return
            find_path(root, [], res)
            find_path_in_tree(root.left, res)
            find_path_in_tree(root.right, res)

        res = []
        find_path_in_tree(root, res)
        answer = []
        for re in res:
            temp = [str(r) for r in re]
            temp_str = "->".join(temp)
            answer.append(temp_str)
        return answer

    def pathSum2(self, root, sum):
        '''
        https://leetcode-cn.com/problems/path-sum-iii/description/
        :param root:
        :param sum:
        :return:
        '''
        def helper(root, sum, now_sum, sum_dict):
            if root is None:
                return
            now_sum += root.val
            self.count += sum_dict.get(now_sum - sum, 0)
            if sum_dict.get(now_sum) is not None:
                sum_dict[now_sum] = sum_dict[now_sum] + 1
            else:
                sum_dict[now_sum] = 1
            helper(root.left, sum, now_sum, sum_dict)
            helper(root.right, sum, now_sum, sum_dict)
            print root.val, root.left, sum_dict, now_sum
            sum_dict[now_sum] = sum_dict[now_sum] - 1

        helper(root, sum, 0, {0: 1})
        return self.count

    def pathSum3(self, root, sum):
        def helper(root, sum, now_sum, sum_dict):
            if root is None:
                return 0
            now_sum += root.val
            count = sum_dict.get(now_sum - sum, 0)
            if sum_dict.get(now_sum) is not None:
                sum_dict[now_sum] = sum_dict[now_sum] + 1
            else:
                sum_dict[now_sum] = 1
            count += helper(root.left, sum, now_sum, sum_dict) + helper(root.right, sum, now_sum, sum_dict)
            print root.val, root.left, sum_dict, now_sum
            sum_dict[now_sum] = sum_dict[now_sum] - 1
            return count

        return helper(root, sum, 0, {0: 1})

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

# root.left.left = TreeNode(0)
root.left.right = TreeNode(6)
root.right.left = TreeNode(4)
root.right.right = TreeNode(9)

solu = Solution()
print solu.pathSum3(root, 8)