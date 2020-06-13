# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:26:18 2019

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        head = ListNode(None)
        temp = head
        while a:
            temp.next = ListNode(a.pop())
            temp = temp.next
        return head.next
        
solu = Solution()

head = ListNode(None)
temp = head
a = [1,2,3,4,5]
#a = []
while a:
#    print(a)
    temp.next = ListNode(a.pop(0))
    temp = temp.next
head = head.next

head = solu.reverseList(head)

while head:
    print(head.val)
    head = head.next
    
#Exception: Type <class '__main__.ListNode'>: Not implemented
#Line 105 in serialize (./python3/__serializer__.py)
#Line 44 in _driver (Solution.py)
#Line 53 in <module> (Solution.py)