# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # ans = l1
        # while l1 and l2:
        #     tmp1 = l1.next
        #     tmp2 = l2.next
        #     l1.next = l2
        #     l1 = tmp1
        #     l2.next = l1
        #     l2 = tmp2
        # if l1:
        #     ans.next = l1
        # if l2:
        #     ans.next = l2
        # return ans
        ans = ListNode(None)
        tmp = ans
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1 #同时赋值了x和next属性
                # tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = l2
                # tmp = tmp.next
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2
        return ans.next


        # L = ListNode(None)
        # temp = L #temp和L关联了起来，temp最后虽然没有了，但是给L造成的改变还是积累下来了
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         temp.next = l1 #temp改变，L会跟着改变
        #         l1 = l1.next
        #         temp = temp.next #tenp重新赋值，它和L的关联也就取消了，但是新的值temp.next原本是和L.next关联的；所以下一步被改变的是L.next
        #     else: # if l2.val <= l1.val: #上面if的产生值会影响下面if的条件判定，所以if-if和if-else还是不一样的
        #         temp.next = l2
        #         l2 = l2.next
        #         temp = temp.next
        # if l1:
        #     temp.next = l1
        # else:
        #     temp.next = l2
        # return L.next #temp.next 