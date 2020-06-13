# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:56:48 2019

@author: Administrator
"""

class Solution:
    def sortArray(self, nums: list) -> list:
#        return self.merge_sort(nums)
#        return self.merge_sort_2(nums)
#        return self.heap_sort(nums)
#        return self.heap_sort_2(nums)
#        return self.quick_sort(nums, 0, len(nums)-1)
        return self.quick_sort_2(nums)
        
    def merge(self, left, right):
        p, q = 0, 0
        ans = []
        while p<len(left) and q<len(right):
            if left[p]<=right[q]:
                ans.append(left[p])
                p += 1
            else:
                ans.append(right[q])
                q += 1
        ans += left[p:]
        ans += right[q:]
        return ans
        
    def merge_sort(self, List):
        if len(List)<=1:
            return List
        else:
            num = len(List) // 2
            left = self.merge_sort(List[:num])
            right = self.merge_sort(List[num:])
            return self.merge(left, right)
        
    def merge_2(self, nums, head, mid, tail):
        i = head
        j = mid + 1
        k = head
        temp = nums.copy() #[0] * len(nums)
        while i<=mid and j<=tail:# and k<=tail:#
            if temp[i] <= temp[j]:
                nums[k] = temp[i]
                i += 1
                k += 1
            else:
                nums[k] = temp[j]
                j += 1
                k += 1
        if i<=mid:
            nums[k:tail+1] = temp[i:mid+1]
        if j<=tail:
            nums[k:tail+1] = temp[j:tail+1]
        
    def merge_sort_2(self, nums):
        m = 1
        while m < len(nums):
            head = 0
            while head < len(nums):
                mid = head+m-1
                tail = min(head+2*m-1, len(nums)-1)
                self.merge_2(nums, head, mid, tail)
                head += 2*m
            m *= 2
        return nums
        
    def adjust_heap(self, List, size, k):
        lchild = 2 * k + 1
        rchild = 2 * k + 2
        Max = k
        if k<size//2:
            if lchild<size and List[lchild]>List[Max]: #这里左右子树的if语句是可以调换的
                Max = lchild
            if rchild<size and List[rchild]>List[Max]: #没有短路效应吗？有短路效应。
                Max = rchild
            if Max != k:
                List[Max], List[k] = List[k], List[Max]
                self.adjust_heap(List, size, Max)
                
    def build_heap(self, List, size):
        for k in range(size//2)[::-1]:
            self.adjust_heap(List, size, k)
        
    def heap_sort(self, List):
        size = len(List)
        self.build_heap(List, size) #
        for k in range(size)[::-1]:
            List[0], List[k] = List[k], List[0]
            self.adjust_heap(List, k, 0) #只要堆顶元素最大，堆在逐渐缩小 #这里能用build吗？ #因为只有0被调换过，所以这里对0操作一次
        return List
    
    def adjust_heap_2(self, nums, size, k):
        lchild = 2*k+1
        rchild = 2*k+2
        Max = k
        while lchild < size:
            if lchild < size and nums[lchild] > nums[Max]:
                Max = lchild
            if rchild < size and nums[rchild] > nums[Max]:
                Max = rchild
            if Max != k:
                nums[Max], nums[k] = nums[k], nums[Max]
            else:
                break
            k = Max
            lchild = 2*k+1
            rchild = 2*k+2
        
    def build_heap_2(self, nums, size):
        for k in range(size//2)[::-1]:
            self.adjust_heap_2(nums, size, k)  
        
    def heap_sort_2(self, nums):
        size = len(nums)
        self.build_heap_2(nums, size)
        for k in range(size)[::-1]:
            nums[0], nums[k] = nums[k], nums[0]
            self.adjust_heap_2(nums, k, 0)
        return nums

    def quick_sort(self, nums, left, right):
        if left >= right:
            return nums
        head = left
        tail = right
        key = nums[left]
        while left < right:
            while left < right and nums[right] >= key:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= key:
                left += 1
            nums[right] = nums[left]
        nums[left] = key
        self.quick_sort(nums, head, left-1)
        self.quick_sort(nums, left+1, tail)
        return nums    

    def quick_sort_2(self, nums):
        if len(nums) < 2:
            return nums
        stack = []
        stack.append(len(nums)-1)
        stack.append(0)
        while stack:
            l = stack.pop()
            r = stack.pop()
            idx = self.partition(nums, l, r)
            if l < idx-1:
                stack.append(idx-1)
                stack.append(l)
            if idx+1 < r:
                stack.append(r)
                stack.append(idx+1)
        return nums
        
    def partition(self, nums, left, right):
        key = nums[left]
        while left < right:
            while left < right and nums[right] >= key:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= key:
                left += 1
            nums[right] = nums[left]
        nums[left] = key
        return left    
        
solu = Solution()
nums = [5,2,3,1]
#nums = [5,1,1,2,0,0]
#nums = [5,1,1,2,0]
nums = [3,7,6,4,1,9]
print(solu.sortArray(nums))