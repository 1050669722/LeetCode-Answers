# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:17:43 2019

@author: Administrator
"""

class Solution:
    def merge(self, intervals):
#        intervals = self.Sort(intervals)
##        length = len(intervals)
##        for k in range(0, length-1):
#        for m in range(0, len(intervals)-1):
##            print(m)
##            print(len(intervals)-1)
##            if m < len(intervals)-1:
##            try:
##                for k in range(0, len(intervals)-1):
##    #                    print(k)
##    #                    print(intervals)
##                    if intervals[m][-1] >= intervals[m+1][0]:
##                        intervals.insert(m, [intervals[m][0], max(intervals[m][-1],intervals[m+1][-1])])
##                        intervals.pop(m+1)
##                        intervals.pop(m+1)
##            except:
##                return intervals
#            if m <= len(intervals)-2:
##                print(m)
##                print(len(intervals))
#                for k in range(0, len(intervals)-m-1):
#    #                    print(k)
#    #                    print(intervals)
##                    print(intervals)
#                    if intervals[m][-1] >= intervals[m+1][0]:
#                        intervals.insert(m, [intervals[m][0], max(intervals[m][-1],intervals[m+1][-1])])
#                        intervals.pop(m+1)
#                        intervals.pop(m+1)
#        return intervals
        intervals = self.MergeSort_fun2(intervals)
        k = -1
        for _ in range(len(intervals)):
#            print(intervals)
            k += 1
            if k == len(intervals) - 1: #intervals[k] == intervals[-1]:
                break
            if intervals[k][-1] >= intervals[k+1][0]:
                intervals.insert(k, [intervals[k][0], max(intervals[k][-1],intervals[k+1][-1])])
                intervals.pop(k+1)
                intervals.pop(k+1)
                k -= 1
            else:
                continue
        return intervals
    
#    def Sort(self, L):
##        print(L)
#        LCopy = L.copy() #L在外面还要用的，所以这里拷贝一下 #不需要深拷贝吗？
#        NewL = []
#        for k in range(len(LCopy)): #len(LCopy)尽管在循环中改变，但是这里只取初始化for循环时的值
##            print(k)
#            idx = self.FindMin(LCopy)
#            NewL.append(LCopy.pop(idx))
##        print(L)
#        return NewL
#        
#    def FindMin(self, L):
#        smallest_idx = 0
#        for k in range(len(L)):
#            if L[smallest_idx][0] > L[k][0]:
#                smallest_idx = k
#        return smallest_idx
        
#    def MergeSort_fun1(self, left, right):
#        result = []
#        i, j = 0, 0
#        while i<len(left) and j<len(right): #注意，左右穿插排列大小 #这里的i, j像是指针
#            if left[i] <= right[j]:
#                result.append(left[i])
#                i += 1
#            else:
#                result.append(right[j])
#                j += 1
#        result += left[i:] #是拼接不能用.append()
#        result += right[j:]
#        return result
#        
#    def MergeSort_fun2(self, List):
#        if len(List) <= 1: #这一判断必须得有，否则一直递归下去，因为底层总会到只含有一个元素的列表
#            return List
#        num = len(List) // 2
#        left = self.MergeSort_fun2(List[:num])
#        right = self.MergeSort_fun2(List[num:])
#        return self.MergeSort_fun1(left, right)
        
    def MergeSort_fun1(self, left, right):
        result = []
        i, j = 0, 0
        while i<len(left) and j<len(right): #注意，左右穿插排列大小 #这里的i, j像是指针
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:] #是拼接不能用.append()
        result += right[j:]
        return result
        
    def MergeSort_fun2(self, List):
        if len(List) <= 1: #这一判断必须得有，否则一直递归下去，因为底层总会到只含有一个元素的列表
            return List
        num = len(List) // 2
        left = self.MergeSort_fun2(List[:num])
        right = self.MergeSort_fun2(List[num:])
        return self.MergeSort_fun1(left, right)
    
#    def merge(self, intervals): 
#       intervals = sorted(intervals,key=lambda x:x[1])
#       for i in range(len(intervals)-1,0,-1):
#       	if intervals[i][0]<=intervals[i-1][1]:
#       		intervals[i-1][1] =max(intervals[i][1],intervals[i-1][1])
#       		intervals[i-1][0] =min(intervals[i][0],intervals[i-1][0])    		
#       		intervals.pop(i) 
#       return intervals
        
#class Solution:
#    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#        if intervals == None:
#            return None
#        if len(intervals) == 0 or len(intervals) == 1:
#            return intervals
#        ret = []
#        intervals.sort()
#        start,end = intervals[0][0],intervals[0][1]
#        for item in intervals[1:]:
#            if item:
#                if item[0] >= start and item[0] <= end and item[1] >= end:
#                    end = item[1]
#                if item[0] > end:
#                    ret.append([start,end])
#                    start = item[0]
#                    end = item[1]
#        ret.append([start,end])
#        return ret

solu = Solution()
#intervals = [[1,3],[2,6],[8,10],[15,18]]
#intervals = [[2,6],[8,10],[1,[3]],[2,6],[15,18]]
#intervals = [[2,6],[8,10],[1,3],[2,6],[15,18]]
#print(solu.merge(intervals))
#print(solu.FindMin(intervals))
#intervals = [[1,1],[1,2]]
intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
#intervals = [[1,4],[1,4]]
nums = [3,2,8,9,7,8,2,1]
#nums = [3,2]
#print(solu.MergeSort_fun2(nums))
print(solu.merge(intervals))



