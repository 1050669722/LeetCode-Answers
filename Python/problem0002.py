# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:19:45 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(): #14:30 - 15:51
    def addTwoNumbers(self, l1, l2):
        temp1, temp2, count = 0, 0, 0
        while l1 or l2:#l1 != None or l2 != None:
            if l1 != None:
                temp1 += l1.val * 10**count
                l1 = l1.next
            if l2 != None:
                temp2 += l2.val * 10**count
                l2 = l2.next
            count += 1
        temp = temp1 + temp2 #(n,r) = divmod(13,10) #[int(i) for i in str(134)]
        temp = [int(i) for i in str(temp)]
#        print(temp)
#        l3 = ListNode(temp[-1]) #c = ListNode
# =============================================================================
#         l3 = ListNode(temp[0])
#         l4 = ListNode(None)
# #        print(l3.val)
# #        count = 0
# #        for k in range(len(temp)-2,-1,-1):
#         for k in range(1,len(temp),1):
# #            print(k)
# #            count += 1
# #            if count == 1:
# #                l3.next = ListNode(temp[k])
# #                print(l3.next.val)
# #            elif count == 2:
# #                l3.next.next = ListNode(temp[k])
# #                print(l3.next.next.val)
#             l4 = l3
# #            l3.next = ListNode(temp[k])
# #            l3 = l3.next
#             l3 = ListNode(temp[k])
#             l3.next = l4
#         List = []
#         while l3 != None:
#             List.append(l3.val)
#             l3 = l3.next
# =============================================================================
        l4 = ListNode(None)
        l3 = l4 #关联
        for k in range(len(temp)-1,-1,-1):
            l3.next = ListNode(temp[k]) #改变属性
            l3 = l3.next #重新赋值 ？？？#旧的l3没有关联了，旧的l3.next有关联 #新的l3有关联
        l4 = l4.next
        List = []
        while l4 != None:
            List.append(l4.val)
            l4 = l4.next
        return List        

#class Solution:
#    def addTwoNumbers(self, l1, l2):
#        """
#        :type l1: ListNode
#        :type l2: ListNode
#        :rtype: ListNode
#        """
#        re = ListNode(0)
#        r=re
#        carry=0
#        while(l1 or l2):
#            x= l1.val if l1 else 0
#            y= l2.val if l2 else 0
#            s=carry+x+y
#            carry=s//10
#            r.next=ListNode(s%10)
#            r=r.next
#            if(l1!=None):l1=l1.next
#            if(l2!=None):l2=l2.next
#        if(carry>0):
#            r.next=ListNode(1)
#        return re.next

solu = Solution()
a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)
b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)
c = solu.addTwoNumbers(a, b)
print(c)
#while c != None:
#    print(c.val)
#    c = c.next
    
#while a != None:
#    print(a.val)
#    a = a.next
#    
#while b != None:
#    print(b.val)
#    b = b.next

time2 = time.perf_counter()
print(time2 - time1)