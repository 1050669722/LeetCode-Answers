# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        low, fast = head, head
        count = 0
        while fast:
            count += 1
            low = low.next
            fast = fast.next.next
        
        pre = None
        cur = low
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        h = head
        p = pre
        # while h and p:
        # while h != low:
        print(count)
        for _ in range(count):
            tmp_h = h.next
            tmp_p = p.next

            h.next = p
            p.next = tmp_h
            h = tmp_h
            p = tmp_p

        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
solu = Solution()
# print(solu.reorderList(head))
ans = solu.reorderList(head)
print('**********')
tmp = ans
while tmp:
    print(tmp.val)
    tmp = tmp.next