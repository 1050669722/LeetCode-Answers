# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        tmp = head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        ind = count // 2
        
        count = 0
        tmp = head
        while tmp:
            if count == ind:
                return tmp
            else:
                count += 1
                tmp = tmp.next


# class Solution(object):
#     def middleNode(self, head):
#         A = [head]
#         while A[-1].next:
#             A.append(A[-1].next)
#         return A[len(A) / 2]

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/middle-of-the-linked-list/solution/lian-biao-de-zhong-jian-jie-dian-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution(object):
    def middleNode(self, head):
        low, fast = head, head
        while fast and fast.next: #如果没有fast，就不会有fast.next
            low = low.next
            fast = fast.next.next #到最后有可能没有fast
        return low



