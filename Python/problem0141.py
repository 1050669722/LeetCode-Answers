# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not (head and head.next):
            return False

        low, fast = head, head.next
        while low != fast:
            if not (fast and fast.next): #此判断语句，是为了当head指向一个非环形链表时，避免循环陷入无限循环
                return False
            low = low.next
            fast = fast.next.next
        return True