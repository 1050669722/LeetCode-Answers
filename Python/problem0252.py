# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:04:53 2019

@author: Administrator
"""

class Solution:
    def canAttendMeetings(self, intervals: list) -> bool:
        if intervals == []:
            return True
        intervals = self.merge_sort(intervals)
        original_intervals = intervals.copy()
        k = -1
        for _ in range(len(intervals)):
            k += 1
#            print(len(intervals))
            if k == len(intervals)-1:
                break
            else:
                if intervals[k][-1] > intervals[k+1][0]:
                    intervals.insert(k, [intervals[k][0], max(intervals[k][-1], intervals[k+1][-1])])
                    intervals.pop(k+1)
                    intervals.pop(k+1)
                    k -= 1
                else:
                    continue
        if intervals == original_intervals:
            return True
        else:
            return False
#        print(original_intervals)
#        return intervals
        
    def merge(self, left, right):
        p, q = 0, 0
        ans = []
        while p<len(left) and q<len(right):
            if left[p][0] <= right[q][0]:
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
        
solu = Solution()
intervals = []
intervals = [[0,30],[5,10],[15,20]]
#intervals = [[7,10],[2,4]]
intervals = [[13,15],[1,13]]
#print(solu.merge_sort(intervals))
print(solu.canAttendMeetings(intervals))