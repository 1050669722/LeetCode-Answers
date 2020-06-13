# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """

#         low, fast = head, head
#         while fast:
#             low = low.next
#             fast = fast.next.next
        
#         pre = None
#         cur = low
#         while cur:
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
        
#         h = head
#         p = pre
#         while h and p:
#             tmp_h = h.next
#             tmp_p = p.next
            
#             h.next = p
#             p.next = tmp_h
#             h = tmp_h
#             p = tmp_p

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        # 1 2 3 4 5
        fast = head
        pre_mid = head
        # 找到中点, 偶数个找到时上界那个
        while fast.next and fast.next.next:
            pre_mid = pre_mid.next
            fast = fast.next.next
        # 翻转中点之后的链表,采用是pre, cur双指针方法
        pre = None
        cur = pre_mid.next
        # 1 2 5 4 3
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 翻转链表和前面链表拼接
        pre_mid.next = pre
        # 1 5 2 4 3
        # 链表头
        p1 = head
        # 翻转头
        p2 = pre_mid.next
        #print(p1.val, p2.val)
        while p1 != pre_mid:
            # 建议大家这部分画图, 很容易理解
            pre_mid.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = pre_mid.next

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/reorder-list/solution/yong-zhan-fan-zhuan-huo-zhe-zhi-jie-fan-zhuan-by-p/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。