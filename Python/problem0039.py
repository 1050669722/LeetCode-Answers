# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:42:03 2019

@author: Administrator
"""

class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        candidates.sort()
        n = len(candidates)
        ans = []
        def backtrack(i, tmp_sum, tmp):
            if i==n or tmp_sum>target:
                return 
            if tmp_sum == target:
                ans.append(tmp)
                return
            for j in range(i, n): #这个索引开头的情况遍历之后，换为下一个索引开头的情况
                if tmp_sum + candidates[j] > target:
                    break #对于已有的组合，还要退返，表现为函数的return,或者出栈；因为前层函数保存了可能的组合
                if j>i and candidates[j] == candidates[j-1]: #在这里，这两行是可以不要的
                    continue #解集不能包含重复的组合。 
                backtrack(j, tmp_sum+candidates[j], tmp+[candidates[j]])
        backtrack(0, 0, [])
        return ans
        
#        candidates.sort()
#        n = len(candidates)
#        res = []
#        def backtrack(i, tmp_sum, tmp):
#            if  tmp_sum > target or i == n: #组合的总和大于目标 或者 索引刚刚超出范围 #组合的元素太多
#                return 
#            if tmp_sum == target: #组合的元素正好 和也相等
#                res.append(tmp)
#                return 
#            for j in range(i, n): #组合的元素太少 #从i开始，说明组合元素是重复的
#                if tmp_sum + candidates[j] > target: #现在的和 加上从这里开始的某一个值 如果太大就跳出循环 #不应该是continue吗？
#                    break #这里为什么是break呢？ 因为后面的数不去遍历它，自然由上层递归去遍历它；而且这里的候选数组已经排好序了，升序，后面的数会越来越大，所以不应该continue，而是return出去，上次那个数不添加进来
#                backtrack(j,tmp_sum + candidates[j],tmp+[candidates[j]]) #现在的和 加上匆匆这里开始的某一个值 如果小于等于目标就再次进入backtrack函数
#        backtrack(0, 0, []) #从第0个元素 组合和为0 组合为[] 开始调用backtrack函数 
#        return res

#作者：powcai
#链接：https://leetcode-cn.com/problems/two-sum/solution/xue-yi-tao-zou-tian-xia-hui-su-suan-fa-by-powcai/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            
solu = Solution()
candidates, target = [2,3,6,7], 7
candidates, target = [2,3,5], 8
print(solu.combinationSum(candidates, target))
