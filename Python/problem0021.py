# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:43:56 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#        temp2 = l2
#        l2 = ListNode(l1.val)
#        l2.next = temp2
#        temp1 = l1
        L = ListNode(None)
        temp = L #temp和L关联了起来，temp最后虽然没有了，但是给L造成的改变还是积累下来了
#        temp = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1 #temp改变，L会跟着改变
                l1 = l1.next
                temp = temp.next #tenp重新赋值，它和L的关联也就取消了，但是新的值temp.next原本是和L.next关联的；所以下一步被改变的是L.next
#                print(1)
            else: # if l2.val <= l1.val: #上面if的产生值会影响下面if的条件判定，所以if-if和if-else还是不一样的
                temp.next = l2
                l2 = l2.next
                temp = temp.next
#                print(2)
#            print(3)
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        return L.next #temp.next 
'''
有的时候可能要写好之后再重构整理
'''
#class Solution:
#    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#        res = ListNode(None)
#        node = res
#        while l1 and l2:
#            if l1.val<l2.val:
#                node.next,l1 = l1,l1.next #所以这样的赋值语句也是按照前后顺序的
#            else:
#                node.next,l2 = l2,l2.next
#            node = node.next
#        if l1:
#            node.next = l1
#        else:
#            node.next = l2
#        return res.next  

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
#a = ListNode(2)
#b = ListNode(1)
solu = Solution()
c = solu.mergeTwoLists(a,b)
while c:
    print(c.val)
    c = c.next

time2 = time.perf_counter()        
print(time2-time1)
