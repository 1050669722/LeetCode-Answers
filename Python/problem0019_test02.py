# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not (head and head.next):
            return None
        tmp = head
        head = ListNode(None)
        head.next = tmp
        low, fast = head, head
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            low = low.next
        low.next = low.next.next
        return head.next

