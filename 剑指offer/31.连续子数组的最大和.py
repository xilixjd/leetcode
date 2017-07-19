# -*- coding:utf-8 -*-
'''
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他忽悠住？(子向量的长度至少是1)
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        '''
        1. 动态规划
        :param array:
        :return:
        '''
        return self.FindGreatestSumOfSubArrayDynamic(array, len(array) - 1)

    def FindGreatestSumOfSubArrayDynamic(self, array, i):
        if i == 0 or self.FindGreatestSumOfSubArrayDynamic(array, i - 1) <= 0:
            return array[i]
        if i != 0 and self.FindGreatestSumOfSubArrayDynamic(array, i - 1) > 0:
            return self.FindGreatestSumOfSubArrayDynamic(array, i - 1) + array[i]

    def f(self, pData):
        greatest = -100000000
        curSum = 0
        for i in range(len(pData)):
            curSum = max(pData[i], curSum + pData[i])
            greatest = max(curSum, greatest)
        return greatest

    def FindGreatestSumOfSubArray2(self, array):
        greatest = -100000000
        curSum = 0
        for i in range(len(array)):
            if curSum <= 0:
                curSum = array[i]
            else:
                curSum += array[i]
            if curSum > greatest:
                greatest = curSum
        return greatest


solu = Solution()
print solu.FindGreatestSumOfSubArray2([1,-2,3,10,-4,7,2,-5])
print solu.f([1,-2,3,10,-4,7,2,-5])