# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:40:52 2019

@author: Administrator
"""

import time 

time1 = time.perf_counter()

#class Solution(): #15:40 - 17:11
#    def removeDuplicates(self, nums):
#        if len(nums) <= 1:
#            return len(nums)
#        else:
#            p = 0
#            q = 0
#            length = len(nums)
#            while p != len(nums)-1:
##                print(p)
##                print(len(nums)-1)
#                for k in range(p, length-1):
#                    print(k)
#                    print(k+1)
#                    print(nums)
#                    if k+1 >= len(nums) or nums[k] != nums[k+1]:
##                        print(nums[k])
##                        print(nums[k+1])
#                        q = k
#                        break
#                if q == 0:
#                    return nums[0] #nums[0]
##                print(q)
#                while (q) != p:
##                    print(p)
##                    print(nums)
##                    print(q)
#                    nums.pop(p)
#                    q -= 1
##                    print(q)
##                    print(q+1 != p)
#                p += 1
#            return nums

#class Solution:
#    def removeDuplicates(self, nums):
#        if(nums==[]):
#            return 0
#        
#        a=nums[0]
#        p=0
#        while(p<len(nums)-1):
#            while((nums[p+1]==a)):
#                del nums[p+1]
#                if(p+1==len(nums)):
#                  break
#
#            p=p+1
#            if (p == len(nums)):
#                break
#            a = nums[p]
#        return len(nums)
    
#class Solution:
#    def removeDuplicates(self, nums: List[int]) -> int:
#        def dedupe(items):
#            seen = set()
#
#            for item in items:
#                if item not in seen:
#                    yield item
#                    seen.add(item)
#
#        index = 0
#        for ele in dedupe(nums):
#            nums[index] = ele
#            index += 1
#
#        return index

class Solution():
    def removeDuplicates(self, nums): #双指针
        '''
        时间复杂度：O(n)，假设数组的长度是 n，那么 i 和 j 分别最多遍历 n 步。
        空间复杂度：O(1)。
        '''
        if nums == []: #只利用原本的数组的空间，就可以省下空间
            return 0
        else:
            i = 0
            for j in range(len(nums)):
                if nums[j] != nums[i]:
                    i += 1
                    nums[i] = nums[j]
            return nums[:i+1] #i+1#

solu = Solution()
#nums = [1,1,2]
#nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1]
#nums = [1,1,1]
nums  = [1,1,2,2]
nums = sorted([3, 2, 6, 1, 7, 0, 3, 1, 4, 0, 1])
#solu.removeDuplicates(nums)
print(solu.removeDuplicates(nums))

time2 = time.perf_counter()
print(time2-time1)
