# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''


class Solution(object):
    def canJump(self, nums):
        """
        https://leetcode.com/problems/jump-game/discuss/20917/Linear-and-simple-solution-in-C++
        https://leetcode.com/problems/jump-game/solution/
        :type nums: List[int]
        :rtype: bool
        """
        reach = i = 0
        while i < len(nums) and i <= reach:
            reach = max(reach, nums[i] + i)
            i += 1
        return i == len(nums)

    def canJump1(self, nums):
        """
        超时
        https://leetcode.com/problems/jump-game/solution/
        :type nums: List[int]
        :rtype: bool
        """
        def jump_next(pos, nums):
            if pos == len(nums) - 1:
                return True
            further = min(pos + nums[pos], len(nums) - 1)
            for i in range(pos + 1, further + 1):
                if jump_next(i, nums):
                    return True
            return False

        return jump_next(0, nums)


solu = Solution()
print solu.canJump1([0,2,3])