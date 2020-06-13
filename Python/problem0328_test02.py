# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # if not (head and head.next and head.next):
        #     return head

        # odd, even = head, head.next
        # ans1 = ListNode(None)
        # a1 = ans1
        # ans2 = ListNode(None)
        # a2 = ans2
        # # tmp = head
        # # while odd and odd.next and even and even.next: #cur是cur.next的前提，现在没有了.next，even或者odd来取代了，所以这样写条件是合理的
        # # while odd and odd.next odd.next.next: #cur是cur.next的前提，现在没有了.next，even或者odd来取代了，所以这样写条件是合理的
        # while odd and odd.next: #cur是cur.next的前提，现在没有了.next，even或者odd来取代了，所以这样写条件是合理的
        #     a1.next = odd
        #     tmp = odd.next
        #     odd.next = odd.next.next
        #     odd = tmp
        #     odd = odd.next
        #     if a1.next:
        #         a1 = a1.next
        # while even and even.next:
        #     a2.next = even
        #     tmp = even.next
        #     even.next = even.next.next
        #     even = tmp
        #     even = even.next
        #     a2 = a2.next
        # a2 = a2.next
        # a1.next = a2
        # return ans1


        if not (head and head.next and head.next):
            return head
            
        oddhead, evenhead = head, head.next
        odd, even = oddhead, evenhead
        while odd and even and even.next:
            tmp1 = odd.next.next
            tmp2 = even.next.next
            odd.next = tmp1
            even.next = tmp2
            odd = tmp1
            even = tmp2
        odd.next = evenhead
        return oddhead
