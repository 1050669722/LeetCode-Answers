# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:47:22 2019

@author: Administrator
"""

class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#        ans = []
#        nums1 = nums1[:m]
#        nums2 = nums2[:n]
#        p, q = 0, 0
#        while p<len(nums1) and q<len(nums2):
#            if nums1[p] <= nums2[q]:
#                ans.append(nums1[p])
#                p += 1
#            else:
#                ans.append(nums2[q])
#                q += 1
#        ans += nums1[p:]
#        ans += nums2[q:]
##        nums1 = ans
#        return ans
#        ans = []
#        nums1 = nums1[:m]
#        nums2 = nums2[:n]
        for k in range(len(nums1)-m):
            nums1.pop()
        for k in range(len(nums2)-n):
            nums2.pop()
        p, q = 0, 0
        while p<len(nums1) and q<len(nums2):
            if nums1[p] <= nums2[q]:
#                ans.append(nums1[p])
                p += 1
            else:
#                ans.append(nums2[q])
                nums1.insert(p, nums2[q])
                q += 1
#        ans += nums1[p:]
#        ans += nums2[q:]
#        nums1 = ans
        temp = nums2[q:]
        while temp:
            nums1.append(temp.pop(0))
        return None
        
        
solu = Solution()
#nums1 = [1,2,3,0,0,0]
#m = 3
#nums2 = [2,5,6]
#n = 3
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
print(solu.merge(nums1, m, nums2, n))
print(nums1)