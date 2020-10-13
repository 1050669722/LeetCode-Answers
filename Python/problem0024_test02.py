# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pre = None
        cur = head
        later = cur.next
        sp = later.next

        while cur and cur.next:
            later.next = cur
            cur.next = sp #cur引用了head，在再次定义cur之前，cur的属性被修改，则head的属性也会相应被修改
            if pre:
                pre.next = later
            else:
                head = later #此时的情况对应头节点，这时将head重新定义到头节点
            pre = cur

            if cur.next:
                cur = cur.next
            if cur.next:
                later = cur.next
                sp = later.next

        return head
