# 堆排序
# 构造最大堆（Build_Max_Heap）：若数组下标范围为0~n，考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆。
# 于是只要从n/2-1开始，向前依次构造大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆。
#
# 堆排序（HeapSort）：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。
# 思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。
#
# 最大堆调整（Max_Heapify）：该方法是提供给上述两个过程调用的。目的是将堆的末端子节点作调整，使得子节点永远小于父节点 。


class Sort():
    def HeapSort(self, aray):
        n = len(aray)
        last_node = int(n / 2 - 1)          # 最后一个叶子节点
        for i in range(last_node, -1 ,-1):  # 构造大根堆
            self.maxHeapify(aray, i, n-1)
        for j in range(n-1, 0, -1):         # 堆(数组)排序
            aray[0], aray[j] = aray[j], aray[0]
            self.maxHeapify(aray, 0, j-1)


    def maxHeapify(self, arry, start, end):
        root = start
        while True:
            child = root * 2 + 1      # 需要调整的节点的子节点
            if child > end:
                break
            if child + 1 <= end and arry[child] < arry[child+1]:
                child += 1
            if arry[root] < arry[child]:
                arry[root], arry[child] = arry[child], arry[root]
                root = child
            else:
                break

if __name__ == '__main__':
    sort = Sort()
    arry = [1, 7, 5, 4, 2, 3, 0]
    sort.HeapSort(arry)
    print(arry)