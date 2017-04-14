'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        my own solution beats 85% python submition !!!
        :type nums: List[int]
        :rtype: int
        """
        maxConsecutive = 0
        temp = 0
        for n in nums:
            if n == 1:
                temp += 1
                if maxConsecutive <= temp:
                    maxConsecutive = temp
            else:
                temp = 0

        return maxConsecutive

    def findMaxConsecutiveOnesFast(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = 0
        maxHere = 0
        for n in nums:
            maxHere = maxHere + 1 if n == 1 else 0
            maxNum = max(maxNum, maxHere)

        return maxNum

solu = Solution()
print solu.findMaxConsecutiveOnes([1,0,1,1,0,1])
print solu.findMaxConsecutiveOnesFast([1,1,0,0,1,1,1,1])
