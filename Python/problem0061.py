# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # if not (head and head.next):
        #     return head

        # tmp = head
        # length = 0
        # while tmp:
        #     length += 1
        #     tmp = tmp.next
        # k %= length

        # for _ in range(k):
        #     tmp = head
        #     head = ListNode(None)
        #     head.next = tmp

        #     low, fast = head, head
        #     for _ in range(2):
        #         fast = fast.next

        #     while fast:
        #         fast = fast.next
        #         low = low.next
            
        #     ans = ListNode(None)
        #     tmp = ans
        #     tmp.next = low.next
        #     low.next = None
        #     tmp = tmp.next
        #     tmp.next = head.next
        #     head = ans.next
        # return head


        if not (head and head.next):
            return head

        tmp = head
        length = 0
        while tmp and tmp.next:
            length += 1
            tmp = tmp.next
        tmp.next = head
        length += 1
        k %= length

        ind = length - k - 1
        count = 0
        tmp = head
        # while tmp:
        #     if count == ind:
        #         t = tmp.next
        #         tmp.next = None
        #         break
        #     count += 1
        #     tmp = tmp.next
        # return t
        while count != ind:
            count += 1
            tmp = tmp.next
        t = tmp.next
        tmp.next = None
        return t

        