# -*- coding: utf-8 -*-
'''
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = -214748366123
        secondMaxNum = -2147483648233
        thirdMaxNum = -21474836482344
        array = [-214748366123, -2147483648233, -21474836482344]
        for n in nums:
            if n > maxNum:
                if not n in array:
                    array.insert(0, n)
                maxNum = array[0]
                secondMaxNum = array[1]
                thirdMaxNum = array[2]
            elif maxNum > n > secondMaxNum:
                if not n in array:
                    array.insert(1, n)
                    secondMaxNum = array[1]
                    thirdMaxNum = array[2]
            elif secondMaxNum > n > thirdMaxNum:
                if not n in array:
                    array.insert(2, n)
                    thirdMaxNum = array[2]
            else:
                if not n in array:
                    array.append(n)
        array.pop()
        array.pop()
        array.pop()
        if len(array) > 2:
            return thirdMaxNum
        else:
            return array[0]

solu = Solution()
print solu.thirdMax([1,-2147483648,2])