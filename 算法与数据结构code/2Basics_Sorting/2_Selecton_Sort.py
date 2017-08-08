# 选择排序
# 时间复杂度o(n^2)
# 选择剩下数中最小的排在最前面

def SelectonSort(alist):
    n = len(alist)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            print(alist)
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]

    return alist


def test():
    alist = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    print(SelectonSort(alist))


if __name__ == '__main__':
    test()