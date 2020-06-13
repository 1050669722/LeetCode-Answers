# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:51:43 2019

@author: Administrator
"""

class Solution():
    def insert(self, intervals: list, newInterval: list) -> list:
#        intervals.append(newInterval)
#        intervals = self.merge_sort(intervals)
#        k = -1
#        for _ in range(len(intervals)):
#            k += 1
#            if k == len(intervals) - 1: break
#            if intervals[k][-1] >= intervals[k+1][0]:
#                intervals.insert(k, [intervals[k][0], max(intervals[k][-1],intervals[k+1][-1])])
#                intervals.pop(k+1)
#                intervals.pop(k+1)
#                k -= 1
#        return intervals
        
#        intervals.append(newInterval)
#        intervals = self.merge_sort(intervals)
#        if intervals == []:
#            intervals.append(newInterval)
#            return intervals
#        if len(intervals) == 1:
#            if intervals[0][0] <= newInterval[0]:
#                intervals.append(newInterval)
#            else:
#                intervals.insert(0, newInterval)
#            if intervals[0][-1] >= intervals[1][0]:
#                intervals.insert(0, [intervals[0][0], max(intervals[0][-1],intervals[1][-1])])
#                intervals.pop(1)
#                intervals.pop(1)
#            return intervals
#        else:
#            head = 0
#            tail = len(intervals) - 1
#            while head < tail:
#                mid = (head + tail) // 2
#                if intervals[mid][0] < newInterval[0]:
#                    head = mid + 1
#                elif intervals[mid][0] > newInterval[0]:
#                    tail = mid - 1
#                else:
#                    break
#            k = mid - 2
#            intervals.insert(mid, newInterval)
#            if (intervals[mid][0] == intervals[mid-1][0] or intervals[mid][0] == intervals[mid+1][0]) and mid-1>=0 and mid+1<=len(intervals)-1:
##                print(1)
#                pass
#            elif intervals[mid][0] < intervals[mid-1][0] and mid-1>=0:
##                print(2)
#    #            print(intervals)
#    #            print(mid)
#                intervals[mid], intervals[mid-1] = intervals[mid-1], intervals[mid]
#                k -= 1
#            elif intervals[mid][0] > intervals[mid+1][0]  and mid+1<=len(intervals)-1:
##                print(3)
##                print(intervals)
##                print(mid)
#                intervals[mid], intervals[mid+1] = intervals[mid+1], intervals[mid]
#                k += 1
#    #        print(intervals)
#            k = -1
#            for _ in range(len(intervals)):
#                k += 1
#                if k == len(intervals) - 1: break
#                if intervals[k][-1] >= intervals[k+1][0]:
#                    intervals.insert(k, [intervals[k][0], max(intervals[k][-1],intervals[k+1][-1])])
#                    intervals.pop(k+1)
#                    intervals.pop(k+1)
#                    k -= 1
#            return intervals
        
        mark = 0
        
        count = 0
        for m in range(len(intervals)):
            if newInterval[0] <= intervals[m][0]:
                mark = m
                count += 1
                break
        if count == 0: mark = len(intervals)
        
        intervals.insert(mark, newInterval)    
            
        k = -1
        for _ in range(len(intervals)):
            k += 1
            if k == len(intervals) - 1: break
            if intervals[k][-1] >= intervals[k+1][0]:
                intervals.insert(k, [intervals[k][0], max(intervals[k][-1],intervals[k+1][-1])])
                intervals.pop(k+1)
                intervals.pop(k+1)
                k -= 1
        return intervals
        
    def merge(self, left, right):
        result = []
        p, q = 0, 0
        while p<len(left) and q<len(right):
            if left[p][0] <= right[q][0]:
                result.append(left[p])
                p += 1
            else:
                result.append(right[q])
                q += 1
        result += left[p:]
        result += right[q:]
        return result
        
    def merge_sort(self, List):
        if len(List) <= 1:
            return List
        else:
            num = len(List) // 2
            left = self.merge_sort(List[:num])
            right = self.merge_sort(List[num:])
            return self.merge(left, right)
        
solu = Solution()
#intervals, newInterval = [[1,3],[6,9]], [2,5]
intervals, newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
#intervals, newInterval = [], [5,7]
intervals, newInterval = [[1,5]], [2,3]
#intervals, newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
print(solu.insert(intervals, newInterval))