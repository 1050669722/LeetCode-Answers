# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # count = 0
        # while head:
        #     count += 1
        #     if count == m:
        #         tmp1 = head
        #     if count == n:
        #         tmp2 = head
        #     head = head.next