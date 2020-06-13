# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # ans = ListNode(None)
        # tmp = ans
        # s = set()
        # while head:
        #     if head.val not in s:
        #         s.add(head.val)
        #         tmp.val = head.val
        #         head = head.next
        #         if head:
        #             tmp.next = ListNode(None)
        #             tmp = tmp.next
        #     else:
        #         head = head.next
        # return ans

        ans = head
        tmp = ans
        while tmp and tmp.next:
            if tmp.next.val != tmp.val:
                tmp = tmp.next
            else:
                tmp.next = tmp.next.next
                # tmp = tmp.next
                # tmp = tmp.next
        return ans