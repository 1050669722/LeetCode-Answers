# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        head = pre
        tmp = head
        carry = 1
        while tmp:
            t = tmp.val
            tmp.val = (t+carry) % 10
            carry = (t+carry) // 10
            if tmp.next:
                tmp = tmp.next
            else:
                break
        if carry:
            tmp.next = ListNode(carry)

        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
