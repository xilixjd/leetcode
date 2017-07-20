# -*- coding:utf-8 -*-
'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # number = 0
        # count = 0
        # while count < index:
        #     number += 1
        #     if self.isUgly(number):
        #         count += 1
        # return number
        if index <= 0:
            return 0
        uglyNumbers = [0 for i in range(index)]
        nextUglyIndex = 1
        uglyNumbers[0] = 1
        multiply2 = multiply3 = multiply5 = 1
        while nextUglyIndex < index:
            minN = min(multiply2 * 2, multiply3 * 3, multiply5 * 5)
            uglyNumbers[nextUglyIndex] = minN
            while multiply2 * 2 <= uglyNumbers[nextUglyIndex]:
                multiply2 += 1
            while multiply3 * 3 <= uglyNumbers[nextUglyIndex]:
                multiply3 += 1
            while multiply5 * 5 <= uglyNumbers[nextUglyIndex]:
                multiply5 += 1
            nextUglyIndex += 1
        return uglyNumbers[nextUglyIndex - 1]


    def isUgly(self, number):
        while number % 2 == 0:
            number /= 2
        while number % 3 == 0:
            number /= 3
        while number % 5 == 0:
            number /= 5
        return True if number == 1 else False


solu = Solution()
print solu.GetUglyNumber_Solution(11)