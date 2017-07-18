# -*- coding:utf-8 -*-
'''

定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''

class Solution:
    def __init__(self):
        self.stack = []
        self.stackMin = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if len(self.stackMin) == 0 or node < self.stackMin[len(self.stackMin) - 1]:
            self.stackMin.append(node)
        else:
            self.stackMin.append(self.stackMin[len(self.stackMin) - 1])

    def pop(self):
        # write code here
        if len(self.stack) > 0 and len(self.stackMin) > 0:
            self.stack.pop()
            self.stackMin.pop()

    def top(self):
        # write code here
        if len(self.stack) > 0 and len(self.stackMin) > 0:
            return self.stack[len(self.stack) - 1]

    def min(self):
        # write code here
        if len(self.stack) > 0 and len(self.stackMin) > 0:
            return self.stackMin[len(self.stackMin) - 1]


solu = Solution()
solu.push(3)
solu.push(2)
solu.push(1)
solu.push(4)
print solu.min()