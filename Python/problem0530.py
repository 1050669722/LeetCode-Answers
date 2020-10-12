# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        ImportError
        ans = sys.maxsize

        nums = [] #如果是二叉搜索树，应该不需要这个额外的O(n)空间
        def worker(TreeNode):
            if not TreeNode:
                return None
            else:
                nums.append(TreeNode.val)
            
            if TreeNode.left:
                worker(TreeNode.left)
            
            if TreeNode.right:
                worker(TreeNode.right)

        worker(root)
        
        nums.sort()

        for i, num in enumerate(nums):
            if i != 0:
                ans = min(num - nums[i - 1], ans)
            if i != len(nums) - 1:
                ans = min(nums[i + 1] - num, ans)

        return ans


