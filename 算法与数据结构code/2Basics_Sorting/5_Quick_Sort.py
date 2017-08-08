# 快速排序
# “核心：快排是一种采用分治思想的排序算法，大致分为三个步骤。
#
# 定基准——首先随机选择一个元素最为基准
# 划分区——所有比基准小的元素置于基准左侧，比基准大的元素置于右侧
# 递归调用——递归地调用此切分过程”
# 时间复杂度 o(lgN*N)

import random


class Sort():
    # 非原地快排
    # 空间复杂度太高
    def quickSort1(self,alist):
        print(alist)
        n = len(alist)
        if n <= 1:
            return alist
        else:
            pivot = alist[0]
            return self.quickSort1([x for x in alist[1:] if x < pivot]) \
        + [pivot] + self.quickSort1([x for x in alist[1:] if x >= pivot])

    # 原地快排
    def quickSort2(self, alist, p, r):
        print(alist)
        if p >= r:
            return
        # 以列表的第一个数为标志数
        i = p
        for j in range(p + 1, r + 1):
            # 小于标志数, 索引位 + 1, 将所有小于标志数的移到左边, 大于表指数的的移到右边
            if alist[j] <= alist[p]:
                i += 1
                alist[i], alist[j] = alist[j], alist[i]
        # 将标志数置于相应的位置
        alist[i], alist[p] = alist[p], alist[i]

        self.quickSort2(alist, p, i - 1)
        self.quickSort2(alist, i + 1, r)

    #随机化版本
    def quickSort3(self, alist, p, r):
        print(alist)
        if p >= r:
            return
        # 以随机数为标志数
        i = random.randint(p, r)
        alist[i], alist[p] = alist[p], alist[i]
        x = alist[p]
        for j in range(p + 1, r + 1):
            # 小于标志数, 索引位 + 1, 将所有小于标志数的移到左边, 大于标志数的的移到右边
            if alist[j] <= x:
                i += 1
                alist[i], alist[j] = alist[j], alist[i]
        # 将标志数置于相应的位置
        alist[i], alist[p] = alist[p], alist[i]

        self.quickSort2(alist, p, i - 1)
        self.quickSort2(alist, i + 1, r)


if __name__ == '__main__':

    alist1 = [1, 3, 2, 8, 3, 2, 0]
    alist2 = [1, 3, 2, 8, 3, 2, 0]
    alist3 = [1, 3, 2, 8, 3, 2, 0]
    sort = Sort()
    # print('alist1\n', sort.quickSort1(alist1))
    # sort.quickSort2(alist2, 0, len(alist2) - 1)
    sort.quickSort3(alist3, 0, len(alist3) - 1)
    # print(alist3)