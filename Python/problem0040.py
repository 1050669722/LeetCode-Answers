# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 15:52:15 2019

@author: Administrator
"""

class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        candidates.sort()
        n = len(candidates)
        ans = []
        def backtrack(i, tmp_sum, tmp):
#            if i==n or tmp_sum>target:
#                return 
            if tmp_sum>target:
                return 
            if tmp_sum == target:
                ans.append(tmp)
                return
            for j in range(i, n): #这个索引开头的情况遍历之后，换为下一个索引开头的情况
                if tmp_sum + candidates[j] > target:
                    break #对于已有的组合，还要退返，表现为函数的return,或者出栈；因为前层函数保存了可能的组合
                if j>i and candidates[j] == candidates[j-1]:
                    continue #解集不能包含重复的组合。 
                backtrack(j+1, tmp_sum+candidates[j], tmp+[candidates[j]])
        backtrack(0, 0, [])
        return ans
    
#        if not candidates:
#            return []
#        candidates.sort()
#        n = len(candidates)
#        res = []
#        def backtrack(i, tmp_sum, tmp_list):
#            if tmp_sum == target:
#                res.append(tmp_list)
#                return 
#            for j in range(i, n):
#                if tmp_sum + candidates[j]  > target : break
#                if j > i and candidates[j] == candidates[j-1]:continue
#                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])
#        backtrack(0, 0, [])    
#        return res

#作者：powcai
#链接：https://leetcode-cn.com/problems/two-sum/solution/xue-yi-tao-zou-tian-xia-hui-su-suan-fa-by-powcai/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
        
        
        
solu = Solution()
candidates, target = [10,1,2,7,6,1,5], 8
candidates, target = [2,5,2,1,2], 5
print(solu.combinationSum2(candidates, target))