# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        ans = ListNode(None)
        pre = ans
        cur = head
        while cur and cur.next: #.next报错的位置不一样，如果不写'cur.next'，则是在while里面报错，如果不写'cur'则是在while判断处报错，报错不是判断为假
            tmp = cur.next #等号两边分别看做整体，关联了起来，下面分析是否是重新定义的时候，也要看做整体，重新定义会取消关联
            cur.next = cur.next.next
            tmp.next = cur

            pre.next = tmp
            pre = pre.next
            pre = pre.next

            cur = cur.next

        return ans.next