# 反转链表

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def reverse_linked_list(self, head):
        # 第一个结点为头结点
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

#双向链表反转

class DListNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

    def reverse_linked_list(self, head):
        curr = None
        while head:
            curr = head
            head = curr.next
            curr.next = curr.prev
            curr.prev = head
        return curr

# 删除链表中某个结点

#pre -> next = pre -> next -> next

# 快慢指针, 判断是否有环

class CircleList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def has_circle(self, head):
        slow = head
        fast = head
        while (slow and fast):
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            if slow == fast:
                break
        if fast and slow and (slow == fast):
            return True
        else:
            return False