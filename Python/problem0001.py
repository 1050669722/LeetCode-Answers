# -*- coding: utf-8 -*-
"""
Created on Sun May 12 11:02:03 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

#class Solution: #start: 11:14 end: 11:33
#    def twoSum(self, nums, target):
#        for p in range(0,len(nums),1):
#            if p == len(nums)-1:
##                print(p)
#                p,q=None,None
#                return [p,q]
#            for q in range(p+1,len(nums),1):
#                if nums[p] + nums[q] == target:
#                    return [p,q]
#
##class Solution: #start: 11:14 end: 11:21
##    def twoSum(self, nums, target):
##        for p in range(0,len(nums),1):
##            for q in range(p+1,len(nums),1):
##                if nums[p] + nums[q] == target:
##                    break
###        print(p,q)
                   
#class Solution:
#    def twoSum(self, nums, target):
#        """
#        :type nums: List[int]
#        :type target: int
#        :rtype: List[int]
#        """
#        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
#        head = 0
#        tail = len(nums) - 1
#        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
#        while sum_result != target:
#            if sum_result > target:
#                tail -= 1
#            elif sum_result < target:
#                head += 1
#            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
#        return [sorted_id[head], sorted_id[tail]]
#        
#    
#class Solution:
#    def twoSum(self, nums, target):
#        """
#        :type nums: List[int]
#        :type target: int
#        :rtype: List[int]
#        """
#        hashmap = {}
#        for index, num in enumerate(nums):
#            another_num = target - num
#            if another_num in hashmap:
#                return [hashmap[another_num], index]
#            hashmap[num] = index
#        return None

#class Solution:
#    def twoSum(self, nums, target):
#        s_id= sorted(range(len(nums)), key = lambda k: nums[k])
#        head = 0
#        tail = len(nums)-1
#        result = nums[s_id[head]] + nums[s_id[tail]]
##        print(1)
#        while result != target:
##            print(head)
##            print(tail)
##            print(result)
##            print(2)
#            if result > target:
#                tail -= 1
#                if head == tail:
#                    return None,None
#                result = nums[s_id[head]] + nums[s_id[tail]]
##                print(3)
#            else:
##                print('_' + str(head))
#                head += 1
##                print('_' + str(head))
#                if head == tail:
#                    return None,None
#                result = nums[s_id[head]] + nums[s_id[tail]]
##                print(4)
#        return [s_id[head], s_id[tail]]
    
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for (index, num) in enumerate(nums): #一个数num，它先选，如果没有选到合适的，则作为被选 #所以这一轮操作其实完成了两种动作 #前面轮操作又会为后面轮操作服务
            another_num = target - num
            if another_num in d:
                return [d[another_num], index]
            else:
                d[num] = index
        return None
        
        
        
        

solu = Solution()
a, b = solu.twoSum([2, 15, 11, 7],9)  
#solu.twoSum([2, 0, 11, 15],9)
print(a,b)     

#nums = [2, 15, 11, 11]
#sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
#print(sorted_id)


time2 = time.perf_counter()
print(time2-time1)







         