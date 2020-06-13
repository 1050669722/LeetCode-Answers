# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        mark = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                mark = 1
                break
        if mark == 0:
            return None
        
        tmp = head
        # count = 0
        while True:
            if tmp == slow:
                return slow
            tmp = tmp.next
            # count += 1
            slow = slow.next
