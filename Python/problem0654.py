# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        max_ = max(nums)
        ind = nums.index(max_)
        root = TreeNode(max_)
        nums1 = nums[:ind]
        nums2 = nums[ind+1:]
        root.left = self.constructMaximumBinaryTree(nums1)
        root.right = self.constructMaximumBinaryTree(nums2)
        return root