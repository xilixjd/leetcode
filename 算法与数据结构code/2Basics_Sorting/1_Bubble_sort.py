# 冒泡排序
# 时间复杂度o(n^2)
# 从第一个到最后一个,两个两个比,把小的排前面
# 将先拍好数列最后的数为最大的数

def BubbleSort(alist):
    n = len(alist)
    for i in range(n):
        # print(alist)
        for j in range(1, n - i):
            print(alist)
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
    return alist


def test():
    alist = [6, 5, 3, 1, 8, 7, 2, 4]
    print(BubbleSort(alist))


if __name__ == '__main__':
    test()