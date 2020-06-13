# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:37:54 2019

@author: Administrator
"""

# class Solution:
#     def findDuplicate(self, nums: list) -> int:
#         nums.sort()
#         for k in range(1, len(nums)):
#             if nums[k] == nums[k-1]:
#                 return nums[k]

# class Solution:
#     def findDuplicate(self, nums: list) -> int:
#         tmp = nums.copy()
#         tmp.sort()
#         for k in range(1, len(tmp)):
#             if tmp[k] == tmp[k-1]:
#                 return tmp[k]
        
# class Solution:
#     def findDuplicate(self, nums: list) -> int:
#         '''
#         时间复杂度：O(n)O(n)。Python 和 Java 都依赖于底层的哈希表，所以插入和查找有固定的时间复杂度。因此，该算法是线性的，因为它由一个执行 NN 次恒定工作的 for 循环组成。
#         空间复杂度：O(n)O(n)，在最坏的情况下，重复元素出现两次，其中一次出现在数组索引 n-1n−1 处。在这种情况下，seen 将包含 n-1n−1 不同的值，因此将占用 O(n)O(n) 空间。
#         '''
#         s = set()
#         for k in range(len(nums)):
#             if nums[k] in s:
#                 return nums[k]
#             s.add(nums[k])
        
class Solution:
    def findDuplicate(self, nums: list) -> int:
        # t = nums[0]
        # h = nums[1]
        # if t == h:
        #     return t
        # while t != h:
        #     t = nums[t]
        #     h = nums[nums[h]]
        #     print(t, h)
        #     if nums[t] == nums[h] and t != h:
        #         return nums[t]
        
        # Find the intersection point of the two runners.
        t = nums[0]
        h = nums[0]
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break
        
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = h#t# #写t或h都可以
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1


            

            

        
solu = Solution()
nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
print(solu.findDuplicate(nums))