# 插入排序
# 时间复杂度o(n^2)
# 前面的(第一个)都是排好序的,后面的都是未排好的
# 将未排好的第一个与前面排好序的对比, 若这个比前数大,比后数小,则插入

def InsertionSort(alist):
    n = len(alist)
    for i in range(1, n):
        key = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > key:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = key
    return alist


def test():
    alist = [1, 2, 3, 5, 2, 3]
    print(InsertionSort(alist))


if __name__ == '__main__':
    test()