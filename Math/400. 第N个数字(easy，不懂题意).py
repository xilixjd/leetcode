# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32为整形范围内 ( n < 231)。

示例 1:

输入:
3

输出:
3
示例 2:

输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
'''


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return False
    #find the pos for the pos-digits region where our n belongs
        pos=0
        while n>pos*pow(10,pos)-(pow(10,pos)-1)/9:
            pos+=1
        newPos=pos-1
  #find the position of n in pos-digits region
        nums,res=divmod((n-newPos*pow(10,newPos)+(pow(10,newPos)-1)/9),pos)
        #if res==0, it means n is the last digit of the target number
        if int(res)==0:
            targetNum=pow(10,newPos)-1+int(nums)
            finList=[int(i) for i in str(targetNum)]
            return finList[-1]
# if res!=0, it means n is the last res digit of the next number after target number
        else:
            targetNum=pow(10,newPos)+int(nums)
            finList=[int(i) for i in str(targetNum)]
            return finList[int(res)-1]

solu = Solution()
print solu.findNthDigit(17)