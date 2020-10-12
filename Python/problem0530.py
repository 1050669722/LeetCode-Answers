# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def getMinimumDifference(self, root: TreeNode) -> int:

#         ImportError
#         ans = sys.maxsize

#         nums = [] #如果是二叉搜索树，应该不需要这个额外的O(n)空间
#         def worker(TreeNode):
#             if not TreeNode:
#                 return None
#             else:
#                 nums.append(TreeNode.val)
            
#             if TreeNode.left:
#                 worker(TreeNode.left)
            
#             if TreeNode.right:
#                 worker(TreeNode.right)

#         worker(root)
        
#         nums.sort()

#         for i, num in enumerate(nums):
#             if i != 0:
#                 ans = min(num - nums[i - 1], ans)
#             # if i != len(nums) - 1:
#                 # ans = min(nums[i + 1] - num, ans)

#         return ans


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        import sys
        ans = sys.maxsize
        pre = -sys.maxsize

        def worker(root):
            nonlocal ans, pre #这里如果换成global，就会提示下面的ans, pre没有定义
            if not root:
                return None
            
            worker(root.left)

            tmp = root.val - pre
            ans = min(ans, tmp)
            pre = root.val

            worker(root.right)

        worker(root)

        return ans

