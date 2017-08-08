# -*- coding:utf-8 -*-
# 归并排序
# 分治思想 时间复杂度o(lgN*N)

class Sort:
    def mergeSort(self, alist):
        n = len(alist)
        if n <= 1:
            return alist

        mid = int(n / 2)
        left = self.mergeSort(alist[:mid])
        # print('left = ' + str(left))
        right = self.mergeSort(alist[mid:])
        # print('right = ' + str(right))

        return self.mergeSortedArray(left, right)


    def mergeSortedArray(self, array_A, array_B):
        sortedArray = []
        len_A = len(array_A)
        len_B = len(array_B)
        l = 0
        r = 0
        while l < len_A and r < len_B:
            if array_A[l] < array_B[r]:
                sortedArray.append(array_A[l])
                l += 1
            else:
                sortedArray.append(array_B[r])
                r += 1
        sortedArray += array_A[l:]
        sortedArray += array_B[r:]

        return sortedArray


if __name__ == '__main__':
    merge_sort = Sort()
    unsortedArray = [6, 4, 3, 9, 1, 0, 3]
    print(merge_sort.mergeSort(unsortedArray))