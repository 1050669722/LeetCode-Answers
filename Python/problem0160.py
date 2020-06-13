# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not (headA and headB):
            return None

        cur = headA
        preA = None #正向从空的节点头开始，逆向就从None开始
        while cur:
            tmp = cur.next
            cur.next = preA
            preA = cur
            cur = tmp
        
        cur = headB
        preB = None
        while cur:
            tmp = cur.next
            cur.next = preB
            preB = cur
            cur = tmp

        tA, tB = preA, preB
        pA, pB = tA, tB
        while tA and tB:
            if tA.val != tB.val:
                break
            else:
                pA, pB = tA, tB
                tA = tA.next
                tB = tB.next
        tA = pA
        tA.next = None

        cur = preA
        head = None
        while cur:
            tmp = cur.next
            cur.next = head
            head = cur
            cur = tmp

        return head