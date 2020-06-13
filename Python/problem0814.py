# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def pruneTree(self, root: TreeNode) -> TreeNode:
        
        # def containsone(r):
        #     if not r:
        #         return None
        #     if r.val == 1:
        #         return True
        #     if containsone(r.left):
        #         return True
        #     if containsone(r.right):
        #         return True
        #     return False
        
        # if not root:
        #     return None

        # if not containsone(root):
        #     return None
        # if not containsone(root.left):
        #     root.left = None
        # if not containsone(root.right):
        #     root.right = None


class Solution(object):
    def pruneTree(self, root):
        # def containsOne(node):
        #     if not node: return False
        #     a1 = containsOne(node.left)
        #     a2 = containsOne(node.right)
        #     if not a1: node.left = None
        #     if not a2: node.right = None
        #     return node.val == 1 or a1 or a2

        # return root if containsOne(root) else None

        def containsOne(node): #一边检查一边剪枝 #变量的名称是node而非root，从这里也能看出这个函数的输入是普通的节点
            # 其实应该先剪枝，再判断，否则就return出去了
            # if not node:
            #     return False
            # if node.val == 1 or containsOne(node.left) or containsOne(node.right):
            #     return True
            # if not containsOne(node.left):
            #     node.left = None
            # if not containsOne(node.right):
            #     node.right = None
            if not node:
                return False
            judge_left = containsOne(node.left)
            judge_right = containsOne(node.right)
            if not judge_left: #判断完，先做剪枝 #如果只判断而不做剪枝可能会容易一些
                node.left = None
            if not judge_right:
                node.right = None
            return node.val==1 or judge_left or judge_right
        if containsOne(root):
            return root
        else:
            return None

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/binary-tree-pruning/solution/er-cha-shu-jian-zhi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。