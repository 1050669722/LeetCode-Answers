# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        d = {}
        tmp = head
        while tmp:
            if tmp.val in d:
                d[tmp.val] += 1
            else:
                d[tmp.val] = 1
        
        tmp = head
        head = ListNode(None)
        head.next = tmp
        pre, cur = head, head.next
        while cur:
            if d[cur.val] == 1:
                cur = cur.next
                pre = pre.next
            else:
                for _ in range(d[cur.val]):
                    cur = cur.next
                pre.next = cur
        return head.next