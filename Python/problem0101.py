# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # if not root:
        #     return True

        # levels = []

        # def helper(node, level):
        #     if len(levels) == level:
        #         levels.append([])
        #     levels[level].append(node.val)
        #     if node.left:
        #         helper(node.left, level+1)
        #     else:
        #         levels.append(None)
        #     if node.right:
        #         helper(node.right, level+1)
        #     else:
        #         levels.append(None)
        #     return None
        
        # helper(root, 0)
        # for lev in levels:
        #     if lev != list(reversed(lev)):
        #         return False
        # return True


        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            else:
                a1 = isMirror(t1.left, t2.right)
                a2 = isMirror(t1.right, t2.left)
                return t1.val == t2.val and a1 and a2

        return isMirror(root, root) #自己和自己比较，自己的左右两边比较