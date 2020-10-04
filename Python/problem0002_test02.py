# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        num1 = int(''.join(reversed([str(n) for n in num1])))

        num2 = []
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        num2 = int(''.join(reversed([str(n) for n in num2])))

        tmp = num1 + num2
        num = []
        while tmp:
            num.append(tmp % 10)
            tmp //= 10

        l = ListNode(0)
        t = l
        for i, n in enumerate(num):
            t.val = n
            if i != len(num) - 1:
                t.next = ListNode(0)
            t = t.next

        return l


        
