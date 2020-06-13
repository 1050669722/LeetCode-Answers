# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:49:44 2019

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#class Solution(object):
#    def sortList(self, head):
#        """
#        :type head: ListNode
#        :rtype: ListNode
#        """
#        a = list()
#        while head:
#            a.append(head.val)
#            head = head.next
##        a = sorted(a)
##        a.reverse()
#        a = sorted(a, reverse = True)
##        print(a)
#        head = ListNode(None)
#        temp = head
#        while temp:
#            temp.next = ListNode(a.pop())
##            print(temp)
#            temp = temp.next
#        return head.next
        
#class Solution:
#    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#        if l1 and l2:
#            if l1.val > l2.val:
#                l1, l2 = l2, l1
#            l1.next = self.mergeTwoLists(l1.next, l2)
#        return l1 or l2
#    
#    def sortList(self, head: ListNode) -> ListNode:
#        if not (head and head.next): return head
#        pre, slow, fast = None, head, head
#        while fast and fast.next: pre, slow, fast = slow, slow.next, fast.next.next
#        pre.next = None
#        return self.mergeTwoLists(*map(self.sortList, (head, slow)))
        
        
        
        
        
        