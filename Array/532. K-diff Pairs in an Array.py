# -*- coding: utf-8 -*-

'''
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j),
where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
'''
import collections


class ReSolution(object):
    def findPairs(self, nums, k):
        """
        超时
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 0
        nums.append(1000000000)
        if k == 0:
            flag = True
            for i in range(len(nums) - 1):
                if nums[i + 1] - nums[i] == 0:
                    if flag:
                        count += 1
                        flag = False
                    else:
                        continue
                else:
                    flag = True
        else:
            for i in range(len(nums) - 1):
                if nums[i + 1] - nums[i] == 0:
                    continue
                for j in range(i + 1, len(nums) - 1):
                    if nums[j] - nums[i] == k:
                        count += 1
                        break
                    if nums[j] - nums[i] > k:
                        break
        return count

    def findPairs2(self, nums, k):
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]) is not None:
                d[nums[i]] = 2
            else:
                d[nums[i]] = 1
        count = 0
        if k == 0:
            for key in d:
                if d[key] == 2:
                    count += 1
        elif k > 0:
            for key in d:
                if d.get(key + k) is not None:
                    count += 1
        else:
            return 0
        return count


re = ReSolution()
print re.findPairs2([1,1,1,], 0)


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            set1 = set(nums)
            set2 = set(n + k for n in nums)
            return len(set1 & set2)
        elif k == 0:
            nums_count_dict = {}
            i = 0
            for n in nums:
                if nums_count_dict.get(n):
                    nums_count_dict[n] += 1
                else:
                    nums_count_dict[n] = 1
                i += 1
            count = 0
            for k in nums_count_dict:
                if nums_count_dict[k] > 1:
                    count += 1
            return count
        else:
            return 0

    def findPairs2(self, nums, k):
        """
        no set and k > 0
        :param nums:
        :param k:
        :return:
        """
        nums_count_dict = {}
        for n in nums:
            if nums_count_dict.get(n):
                nums_count_dict[n] += 1
            else:
                nums_count_dict[n] = 1
        count = 0
        for key in nums_count_dict:
            if nums_count_dict.get(key + k):
                count += 1
        return count


    def findPairsFast(self, nums, k):
        if k > 0:
            return len(set(nums) & set(n + k for n in nums))
        elif k == 0:
            return sum(v > 1 for v in collections.Counter(nums).values())
        else:
            return 0

solu = Solution()
# print solu.findPairs([1,2,2,1,1], 0)
# print solu.findPairs2([1,2,3,1,4,2], 2)
# print solu.findPairsFast([3,1,4,1,5], 2)