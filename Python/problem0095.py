# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def generateTrees(self, n: int) -> list:
#         for num in range(1, n+1):
#             Tree = TreeNode(num)
#             Tree.left = self.buildTree( list(range(1,num)) )
#             Tree.right = self.buildTree( list(range(num+1,n+1)) )


#     def buildTree(self, nums):
#         if not nums:
#             return None
        
#         for k in range(len(nums)):
#             Tree = TreeNode(nums[k])
#             Tree.left = self.buildTree( nums[1:k] )
#             Tree.right = self.buildTree( nums[k+1:] )
#         Tree = TreeNode()


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> list:
        if n <= 0:
            return None
        def buildTrees(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end+1):
                LeftTree = buildTrees(start, i-1) # "未来由现在决定，现在由未来产生"
                RightTree = buildTrees(i+1, end)
                for p in LeftTree: #上面的return [None]，意味着这里一定是列表
                    for q in RightTree:
                        Tree = TreeNode(i) #重新定义，意味着左右子树重新清空
                        Tree.left = p
                        Tree.right = q
                        all_trees.append( Tree )
            return all_trees
        return buildTrees(1, n)

    def TreeNum(self, NodeNum):
        dp = [0] * (NodeNum+1)
        dp[0] = 1
        for k in range(1, NodeNum+1):
            dp[k] = (4*k+2)/(k+2) * dp[k-1]
        return dp[NodeNum]





