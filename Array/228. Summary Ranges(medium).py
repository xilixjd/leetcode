# -*- coding: utf-8 -*-
'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
'''


class ReSolution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.append(-100000000)
        res = []
        temp_left = temp_right = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                temp_right += 1
            else:
                if temp_left != temp_right:
                    res.append(str(temp_left) + "->" + str(temp_right))
                else:
                    res.append(str(temp_left))
                temp_left = temp_right = nums[i + 1]
        return res

re = ReSolution()
print re.summaryRanges([])


class Solution(object):
    def summaryRangesMy(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        range1 = 0
        range2 = 0
        array = []
        if len(nums) == 0:
            return []
        for i in range(len(nums)):
            if i == 0:
                range1 = nums[0]
                continue
            if nums[i] - nums[i - 1] == 1:
                continue
            else:
                range2 = nums[i - 1]
                if range1 == range2:
                    array.append(str(range1))
                else:
                    array.append(str(range1) + '->' + str(range2))
                range1 = nums[i]
        range2 = nums[-1]
        if range1 == range2:
            array.append(str(range1))
        else:
            array.append(str(range1) + '->' + str(range2))
        return array

    def summaryRanges(self, nums):
        ranges, r = [], []
        for n in nums:
            if n - 1 not in r:
                r = []
                # ranges.append(r)
                ranges += r,
            # 如果 r[0] 不存在则 r[0]=n，否则r[1] = n
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

solu = Solution()
print solu.summaryRanges([-1, 0, 1, 4, 5, 6, 9, 10])