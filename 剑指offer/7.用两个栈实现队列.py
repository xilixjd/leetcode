# -*- coding:utf-8 -*-
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if len(self.stack2) <= 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) == 0:
            return False
        return self.stack2.pop()

solu = Solution()
solu.push(1)
solu.push(2)
solu.push(3)
print solu.pop()
solu.push(4)
print solu.pop()
