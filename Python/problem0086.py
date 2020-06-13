# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # if not (head and head.next):
        #     return head
        
        # LN1, LN2 = ListNode(None), ListNode(None)
        # l1, l2 = LN1, LN2
        # tmp = head
        # while tmp:
        #     if tmp.val < x:
        #         l1.next = ListNode(tmp.val)
        #         l1 = l1.next
        #     else:
        #         l2.next = ListNode(tmp.val)
        #         l2 = l2.next
        #     tmp = tmp.next

        # # return LN1
        # # return LN2
            
        # if not LN1.next:
        #     return LN2.next
        # if not LN2.next:
        #     return LN1.next

        # tmp = LN1
        # tmp = tmp.next
        # while tmp and tmp.next:
        #     tmp = tmp.next
        # tmp.next = LN2.next
        # return LN1.next

        if not (head and head.next):
            return head

        before, after = ListNode(None), ListNode(None)
        b, a = before, after
        tmp = head
        while tmp:
            t = tmp.next
            tmp.next = None
            if tmp.val < x:
                b.next = tmp
                b = b.next
            else:
                a.next = tmp
                a = a.next
            tmp = t

        if not before.next:
            return after.next
        if not after.next:
            return before.next

        b = before
        while b and b.next:
            b = b.next
        b.next = after.next
        return before.next