# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # vals = []
        # while head:
        #     vals.append(head.val)
        #     head = head.next
        # # print(vals)
        # ans = ListNode(None)
        # tmp = ans
        # while vals:
        #     tmp.val = vals.pop()
        #     if vals:
        #         tmp.next = ListNode()
        #         tmp = tmp.next
        # return ans

        pre = None
        cur = head
        while cur:
            tmp = cur.next

            cur.next = pre

            pre = cur
            
            cur = tmp
        return pre

