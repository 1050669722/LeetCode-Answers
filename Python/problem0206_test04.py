# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            
            cur.next = pre
            pre = cur #关联-修改也被拆开了
            
            cur = tmp #每轮cur都被重新定义了 #cur = cur.next被拆开了
            # tmp.next = cur

            # print(pre.val, cur.val)

        return pre
