# -*- coding:utf-8 -*-

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        p1 = 0
        p2 = len(rotateArray) - 1
        while rotateArray[p1] >= rotateArray[p2]:
            if p2 - p1 == 1:
                return rotateArray[p2]
            mid = (p1 + p2) / 2
            if rotateArray[mid] >= rotateArray[p1]:
                p1 = mid
            elif rotateArray[mid] <= rotateArray[p2]:
                p2 = mid
        return rotateArray[mid]

solu = Solution()
print solu.minNumberInRotateArray([5,6,7,1,2,4])