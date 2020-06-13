# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:11:15 2019

@author: Administrator
"""

#class Solution: #19:13 - 19:25
#    def removeElement(self, nums, val):
#        p = 0
#        length = len(nums)
#        while p != length and length >= 0:
#            p += 1
#            for k in range(len(nums)):
#                if nums[k] == val:
#                    nums.pop(k)
#                    break
#        return len(nums) #return len(nums)

class Solution(): #双指针
    def removeElement(self, nums, val):
        '''
        时间复杂度：O(n)， 假设数组总共有 n 个元素，i 和 j 至少遍历 2n 步。
        空间复杂度：O(1)。
        '''
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
#                print(i,j)
                nums[i] = nums[j]
                i += 1
        return i #nums[:i]

#class Solution():
#    def removeElement(self, nums, val):
#'''
#Java 交换元素？
#时间复杂度：O(n)，i 和 n 最多遍历 n 步。在这个方法中，赋值操作的次数等于要删除的元素的数量。因此，如果要移除的元素很少，效率会更高。
#空间复杂度：O(1)。
#'''
##public int removeElement(int[] nums, int val) {
##    int i = 0;
##    int n = nums.length;
##    while (i < n) {
##        if (nums[i] == val) {
##            nums[i] = nums[n - 1];
##            // reduce array size by one
##            n--;
##        } else {
##            i++;
##        }
##    }
##    return n;
##}

solu = Solution()
#nums = [3,2,2,3]
#val = 3
nums, val = [0,1,2,2,3,0,4,2], 2
#nums, val = [2], 2
#nums, val = [], 2
print(solu.removeElement(nums, val))
