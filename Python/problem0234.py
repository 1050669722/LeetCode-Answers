# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:49:29 2019

@author: Administrator
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
#        if head == None:
#            return False
#        a = []
#        while head:
#            a.append(head.val)
#            head = head.next
##        print(a)
#        a = [str(i) for i in a]
##        print(a)
##        print(''.join(a))
#        a = int(''.join(a))
#        if a < 0 or (a % 10 == 0 and a != 0):
#            return False
#        else:
#            R = 0
#            while a > R:
#                R = 10*R + a%10
#                a //= 10
#            return a==R or a==R//10
        if head == None:
            return True
        a = []
        while head:
            a.append(head.val)
            head = head.next
        b = a.copy()
        b.reverse()
        return a == b
        
solu = Solution()

#a = [1,2]
#a = [1,2,2,1]
#a = []
a = [-129,-129]
L = ListNode(None)
temp = L
while a:
    temp.next = ListNode(a.pop(0))
    temp = temp.next
L = L.next

print(solu.isPalindrome(L))

while L:
    print(L.val)
    L = L.next