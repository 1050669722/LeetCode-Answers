# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:16:25 2019

@author: Administrator
"""

class Solution:
    def summaryRanges(self, nums: list) -> list:
        if nums == []:
            return nums
        a = [nums[0]]
        for k in range(1, len(nums)):
            if type(a[-1]) != list and nums[k] - a[-1] == 1:
                a.append([a[-1], nums[k]])
                a.pop(-2)
            elif type(a[-1]) == list and nums[k] - a[-1][-1] == 1:
                a.append([a[-1][-1], nums[k]])
            else:
                a.append(nums[k])
        
        k = -1
        for _ in range(len(a)):
#            print(a)
            k += 1
#            print(k)
            if k == len(a) - 1: #a[k] == a[-1]:
                break
            if (type(a[k])==list) * (type(a[k+1])==list) == 1:
#                print(a)
#                if k == len(a) - 1: #a[k] == a[-1]:
#                    break
                if a[k][-1] >= a[k+1][0]:
                    a.insert(k, [a[k][0], max(a[k][-1],a[k+1][-1])])
                    a.pop(k+1)
                    a.pop(k+1)
                    k -= 1
#                    print(a)
                else:
                    continue
        
#        for k in a:
#            if type(k) == int:
#                a.insert(0, str(k))
#            else:
#                a.insert(0, str(k[0])+'->'+str(k[-1]))
                
#        for k in range(len(a)):
#            print(a)
#            if type(a[k]) == int:
#                a.insert(0, str(a[k]))
#                a.pop(1)
#            else:
#                a.insert(0, str(a[k][0])+'->'+str(a[k][-1]))
#                a.pop(1)
#        
#        return a.reverse()
                    
#        b = []
#        for k in range(len(a)):
##            print(a)
#            if type(a[k]) == int:
#                b.append(str(a[k]))
#            else:
#                b.append(str(a[k][0])+'->'+str(a[k][-1]))
                    
        b = []
        for k in a:
#            print(a)
            if type(k) == int:
                b.append(str(k))
            else:
                b.append(str(k[0])+'->'+str(k[-1]))
        
        return b
                
solu = Solution()
nums = [0,1,2,4,5,7]
#nums = [0,2,3,4,6,8,9]
#nums = []
#nums = [0,0,0,0,0,0]
print(solu.summaryRanges(nums))