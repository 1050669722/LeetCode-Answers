# -*- coding: utf-8 -*-
"""
Created on Wed May 29 19:33:02 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
#        if root == None:
#            return []
#        a = []
#        PrintTree(root)
#        self.Tree2List(root, a)
#        print(a)
#        a.reverse()
##        print(a)
#        T = Build(a)
#        return T
        
        if root == None:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
        
    def Tree2List(self, root, a):
        if root == None:
            print(-1)
            a.append(None) #return
            return
#        if root.left != None:
        self.Tree2List(root.left, a) #PrintTree(root.left)
        a.append(root.val) #print(root.val)
#        if root.right != None:
        self.Tree2List(root.right, a) #PrintTree(root.right)
        return a
        
def Build(List):
    if List == []:
        return #None
    num = len(List) // 2
    Tree = TreeNode(List[num])
    Tree.left = Build(List[:num])
    Tree.right = Build(List[num+1:])
    return Tree

def PrintTree(Tree):
    if Tree == None:
#        print(None)#return
        return
    if Tree.left != None:
        PrintTree(Tree.left)
    print(Tree.val)
    if Tree.right != None:
        PrintTree(Tree.right)
        
if __name__ == '__main__':
    List = [1,2,3,4,5,6,7,8,9,10]
    List = [1,2]
#    List = []
    T = Build(List)
    solu = Solution()
    T = solu.invertTree(T)
    PrintTree(T)