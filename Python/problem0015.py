# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:40:30 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

#class Solution(): #17:43 - 
#    def threeSum(self, nums):
#        a = []
#        d = {}
#        for (index1, num1) in enumerate(nums):
#            for (index2, num2) in enumerate(nums):
#                if index2 <= index1:
#                    continue
#                another_num = 0 - num1 - num2
#                if another_num in d:
##                    print(d[another_num])
##                    print(index1)
##                    print(index2)
#                    a.append( [d[another_num], index1, index2] )
#                else:
#                    d[num2] = index2
#        b = []
#        for p in a:
#            b.append([ nums[p[0]],nums[p[1]],nums[p[2]] ])
#        return b

#class Solution(): #17:43 - 18:29
#    def threeSum(self, nums):
#        a = []
#        for i in range(len(nums)):
#            for j in range(len(nums)):
#                if j > i:
#                    for k in range(len(nums)):
#                        if k > j:
#                            if nums[i] + nums[j] + nums[k] == 0:
#                                a.append([nums[i], nums[j], nums[k]])
#        for p in range(len(a)):
#            a[p] = sorted(a[p])
#        b = []
#        for q in a:
#            if q not in b:
#                b.append(q)
#        return b

#class Solution(): #17:43 - 18:29
#    def threeSum(self, nums):
#        ans = []
#        for k in range(len(nums)):
#            target = 0 - nums[k]
#            d = {}
#            for p in range(len(nums)):
#                if p != k:
#                    another_number = target - nums[p]
#                    try:
#                        if d[another_number] != k:
#                            ans.append( (nums[d[another_number]], nums[p], nums[k]) )
#                    except:
#                        d[nums[p]] = p
#        return ans


#class Solution():
#    def threeSum(self, nums):
#        nums.sort()
#        ans = []
#        for k in range(len(nums)):
#            head = 0
#            tail = len(nums)-1
#            while head < tail:
#                if nums[k] + nums[head] + nums[tail] == 0:
#                    if head != k and tail != k:
#                        ans.append( (nums[k], nums[head], nums[tail]) )
#                    head += 1
#                    tail -= 1
#                elif nums[k] + nums[head] + nums[tail] < 0:
#                    head += 1
#                else:
#                    tail -= 1
#        return ans

class Solution():
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        #print(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    tmp = [nums[i],nums[left],nums[right]]
                    res.append(tmp)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res


solu = Solution()    
nums = [13,5,-4,-9,1,-3,10,-7,7,3,1,-13,-11,7,-10,12,-15,13,5,-8,-11,-12,-15,-13,-3,-13,5,-4,6,1,-10,4,13,-7,3,-9,-3,-2,-1,12,9,-15,14,5,0,-10,-5,-8,-12,-15,-1,-8,11,-9,-14,-7,-6,7,-4,-15,-15,-7,-4,14,1,6,12,14,12,-11,11,-2,11,2,-12,-4,7,-2,-5,10,-9,10,9,-13,-14,11,-13,-13,3,-1,9,3,7,-9,-6,-14,4,-8,7,1,-12,-5,14,14,12,10,-12,-3,-7,-2,-8,-9,-7,9,-7,-13,5,-12,-11,-7,2,14,3,-14]#[-1, 0, 1, 2, -1, -4]
print(solu.threeSum(nums))
print(len(solu.threeSum(nums)))

time2 = time.perf_counter()
print(time2-time1)
