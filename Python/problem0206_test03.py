# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp = head
        pre = None
        while tmp:
            # t = tmp
            # tmp.next = pre #tmp属性的改变，t会跟着改变
            # pre = tmp
            # tmp = t.next

            t = tmp.next
            tmp.next = pre #tmp.next的重新定义，所以想要不改变t就得使用重新定义
            pre = tmp
            tmp = t
        return pre





