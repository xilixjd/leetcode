# python自带Queue

queue = []
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0)   #return 1
queue[0]  #return 2


# Prioryty Queue 优先队列

'''
\               methods           time complexity
enqueue     heapq.push(queue, e)    O(log n)
dequeue     heapq.pop(queue)        O(log n)
init        heapq.heapify(queue)    O(n log n)
peek        queue[0]                O(1)
'''

# Dequeue 双端队列
# import collection
# dq = collection.dequeue()

'''
\                   methods           time complexity
enqueue left    dq.appendleft(e)          O(1)
enqueue right   dq.append(e)              O(1)
dequeue left    dq.popleft()              O(1)
dequeue right   dq.pop()                  O(1)
peek left       dq[0]                     O(1)
peek right      dq[-1]                    O(1)
'''