# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # if not (head and head.next):
        #     return None

        # length = 0
        # tmp = head
        # while tmp:
        #     length += 1
        #     tmp = tmp.next

        # if n == length:
        #     return head.next

        # ind = length - n
        # tmp = head
        # count = 0
        # while tmp:
        #     if count == ind - 1:
        #         tmp.next = tmp.next.next
        #         return head
        #     else:
        #         tmp = tmp.next
        #     count += 1


        if not (head and head.next):
            return None

        tmp = head
        head = ListNode(None)
        head.next = tmp
        low, first = head, head

        # while first:
        #     mark = 1
        #     tmp = low
        #     for _ in range(n+1):
        #         if first:
        #             first = first.next
        #             low = first
        #         else:
        #             mark = 0
        #             break
        #     if mark == 0:
        #         low = tmp
        
        tmp = low
        for _ in range(n+1): #先撑开一段距离
            first = first.next

        while first:
            first = first.next
            low = low.next
        low.next = low.next.next
        return head.next