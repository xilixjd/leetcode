# -*- coding: utf-8 -*-
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
 The algorithm should run in linear time and in O(1) space.
'''

import math


class ReSolution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return nums[:1]
            else:
                return nums
        apears = int(math.floor(len(nums) / 3)) + 1
        nums.sort()
        res = []
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
                if count >= apears and nums[i] not in res:
                    res.append(nums[i])
            else:
                count = 1
        return res


    def majorityElement2(self, nums):
        """
        最多只可能有两个数
        https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []
        n1 = n2 = nums[0]
        count1 = count2 = 0
        for n in nums:
            if n == n1:
                count1 += 1
            elif n == n2:
                count2 += 1
            elif count1 == 0:
                n1 = n
                count1 += 1
            elif count2 == 0:
                n2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        print n1, n2, count1, count2
        count1 = count2 = 0
        for n in nums:
            if n == n1:
                count1 += 1
            elif n == n2:
                count2 += 1
        if count1 > len(nums) / 3:
            res.append(n1)
        if count2 > len(nums) / 3:
            res.append(n2)
        return res


re = ReSolution()
print re.majorityElement2([1])


class Solution(object):
    def majorityElementMy(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        nums_dict = {}
        array = []
        appear_time = math.floor(nums_len / 3) + 1
        for i in range(nums_len):
            if nums_dict.get(nums[i]) is None:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1
        for k in nums_dict:
            if nums_dict[k] >= appear_time:
                array.append(k)
        return array

    def majorityElementFast(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]

solu = Solution()
print solu.majorityElementMy([1,1,3,1])