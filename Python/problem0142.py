# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # if not (head and head.next):
        #     return None

        # low = head
        # tmp = low
        # fast = head.next
        # # count = 0
        # while low != fast:
        #     if not (fast and fast.next):
        #         return None
        #     tmp = low
        #     low = low.next
        #     fast = fast.next.next
        #     # count += 1
        # # return count-1
        # return tmp

        if not (head and head.next):
            return None

        low, fast = head, head
        mark = 0
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if low == fast:
                mark = 1
                break
        if mark == 0:
            return None

        tmp = head
        while True:
            if tmp == low:
                return low
            tmp = tmp.next
            low = low.next