# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:58:47 2019

@author: Administrator
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
#        tmp = [int(x) for x in str(num)]
#        for k in range(len(tmp)):
#            if tmp[k] == max(tmp[k:]):
#                pass
#            else:
##                print(tmp)
##                print(k, max(tmp[k:]))
##                print(-1)
##                print(tmp[k])
##                print(tmp[tmp.index(max(tmp[k:]))])
#                idx = tmp[k:].index(max(tmp[k:]))
##                print(idx)
#                temp = tmp[k:]
#                temp[0], temp[idx] = temp[idx], temp[0]
#                tmp = tmp[:k] + temp
##                tmp[k], tmp[k:][idx] = tmp[k:][idx], tmp[k]
##                tmp[k:][0], tmp[k:][idx] = tmp[k:][idx], tmp[k:][0]
##                tmp[k], tmp[tmp.index(max(tmp[k:]))] = tmp[tmp.index(max(tmp[k:]))], tmp[k]
##                tmp[k], tmp[k:][tmp[k:].index(max(tmp[k:]))] = tmp[k:][tmp[k:].index(max(tmp[k:]))], tmp[k]
##                print(tmp[k])
##                print(tmp[tmp.index(max(tmp[k:]))])
#                break
#        tmp = [str(x) for x in tmp]
#        tmp = ''.join(tmp)
#        return int(tmp)
        
        nums = list(str(num))
        nums2 = sorted(nums, reverse=True)
        if nums == nums2:
            return num
        else:
            for i in range(len(nums)):
                if nums[i] != nums2[i]:
                    j = -1-nums[::-1].index(nums2[i])
                    nums[i],nums[j] = nums[j],nums[i]
                    break
        return int(''.join(nums))
        
solu = Solution()
num = 2736
#num = 9973
#num = 0
#num = 98368
num = 1993
num2= 9931
print(solu.maximumSwap(num))
