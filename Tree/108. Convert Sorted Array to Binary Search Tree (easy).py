'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ReSolution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(nums, low, high):
            if low > high:
                return
            mid = (low + high) / 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, low, mid - 1)
            root.right = dfs(nums, mid + 1, high)
            return root

        return dfs(nums, 0, len(nums) - 1)

re = ReSolution()
print re.sortedArrayToBST([1,2,3,4,5]).val


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, start, right):
        if start > right:
            return
        mid = (start + right) / 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, start, mid - 1)
        root.right = self.dfs(nums, mid + 1, right)
        return root

# solu = Solution()
# print solu.sortedArrayToBST([1,2,3,4,5]).right.val