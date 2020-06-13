# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            if head.val == val:
                return None
            else:
                return head
        tmp = head
        while tmp.next: #阻止最后一些节点的遍历
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next #到最后依然会后tmp
            # tmp = tmp.next
        if head.val != val:
            return head
        else:
            return head.next