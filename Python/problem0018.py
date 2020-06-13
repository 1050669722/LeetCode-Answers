# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:32:37 2019

@author: Administrator
"""

class Solution():
    def fourSum(self, nums: list, target: int) -> list:
        nums = self.merge_sort(nums)
        ans = []
        for i in range(len(nums)):
#            if i>0:
#                print(i,j,p,q)
#                if [nums[i],nums[j],nums[p],nums[q]] == [nums[i-1],nums[j],nums[p],nums[q]]:
#                    continue
            for j in range(i+1, len(nums)):
#                if j>1: 
#                    if [nums[i],nums[j],nums[p],nums[q]] == [nums[i],nums[j-1],nums[p],nums[q]]:
#                        continue
                p = j+1
                q = len(nums)-1
                while p<q:
                    if nums[i]+nums[j]+nums[p]+nums[q] == target:
                        ans.append([nums[i],nums[j],nums[p],nums[q]])
#                        p += 1
#                        q -= 1
                        temp = [nums[i],nums[j],nums[p],nums[q]]
                        while temp == [nums[i],nums[j],nums[p],nums[q]] and p<q: #在循环内改循环条件要注意条件限制
                            p += 1
                    elif nums[i]+nums[j]+nums[p]+nums[q] < target:
                        temp = [nums[i],nums[j],nums[p],nums[q]]
                        while temp == [nums[i],nums[j],nums[p],nums[q]] and p<q:
                            p += 1
                    else:
                        temp = [nums[i],nums[j],nums[p],nums[q]]
                        while temp == [nums[i],nums[j],nums[p],nums[q]] and p<q:
                            q -= 1
#        print(':')
#        print(ans)
        if ans == []:
#            print(1)
            return []
        ans_new = []
        for k in ans:
            if k not in ans_new:
                ans_new.append(k)
        return ans_new
#        return ans
#        if ans == []:
#            return []
#        else:
##            m, n = 0, 0
##            ans = sorted(ans, key=lambda a: a[0])
##            for n in range(len(ans)):
##                if ans[n][0] != ans[m][0]:
##                    m = n
#                
#            p = 0
#            for q in range(len(ans)):
#                if ans[q] != ans[p]:
#                    p += 1
#                    ans[p] = ans[q]
#            return ans[:p+1]
        
        if nums == []: #只利用原本的数组的空间，就可以省下空间
            return 0
        else:
            i = 0
            for j in range(len(nums)):
                if nums[j] != nums[i]:
                    i += 1
                    nums[i] = nums[j]
            return i+1#nums[:i+1]
        
    def merge(self, left, right):
        result = []
        p, q = 0, 0
        while p<len(left) and q<len(right):
            if left[p] <= right[q]:
                result.append(left[p])
                p += 1
            else:
                result.append(right[q])
                q += 1
        result += left[p:]
        result += right[q:]
        return result
        
    def merge_sort(self, List):
        if len(List) <= 1:
            return List
        else:
            num = len(List) // 2
            left = self.merge_sort(List[:num])
            right = self.merge_sort(List[num:])
            return self.merge(left, right)
        
solu = Solution()
nums, target = [1, 0, -1, 0, -2, 2], 0
nums, target = [], 0
nums, target = [-3,-2,-1,0,0,1,2,3], 0
#nums, target = [0,0,0,0], 0
#nums, target = [-487,-462,-445,-401,-389,-388,-379,-374,-365,-334,-326,-314,-302,-280,-277,-241,-234,-216,-207,-179,-154,-130,-118,-102,-98,-37,-30,-19,13,21,22,61,66,83,84,109,117,122,141,162,170,205,209,223,232,240,246,250,264,274,286,289,303,304,322,335,336,338,349,355,360,363,365,397,403,417,420,429,438,439], 1801
#ans=solu.fourSum(nums, target)
#nums, target = [-1,0,1,2,-1,-4], -1
nums, target = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5], 0
print(solu.fourSum(nums, target))
print(solu.merge_sort(nums))


