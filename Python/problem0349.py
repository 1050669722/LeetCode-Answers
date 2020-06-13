# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:58:47 2019

@author: Administrator
"""

class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
#        if nums1 == [] or nums2 == []:
#            return []
#        nums1 = self.merge_sort(nums1)
#        nums2 = self.merge_sort(nums2)
#        nums1 = self.deleteDuplicate(nums1)
#        nums2 = self.deleteDuplicate(nums2)
#        d = {}
#        a = []
#        for k in nums1:
#            try:
#                d[k] += 1
#            except:
#                d[k] = 1
#        for k in nums2:
#            try:
#                d[k]
#                a.append(k)
#            except:
#                pass
#        return a
        return list(set(nums1) & set(nums2))
        
    def merge(self, left, right):
        p, q = 0, 0
        ans = []
        while p<len(left) and q<len(right):
            if left[p] <= right[q]:
                ans.append(left[p])
                p += 1
            else:
                ans.append(right[q])
                q += 1
        ans += left[p:]
        ans += right[q:]
        return ans
    
    def merge_sort(self, List):
        if len(List) <= 1:
            return List
        else:
            num = len(List) // 2
            left = self.merge_sort(List[:num])
            right = self.merge_sort(List[num:])
            return self.merge(left, right)
        
    def deleteDuplicate(self, nums):
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
nums1, nums2 = [1,2,2,1], [2,2]
#nums1, nums2 = [4,9,5], [9,4,9,8,4]
#nums1, nums2 = [1,2,2,1], []
print(solu.intersection(nums1, nums2))