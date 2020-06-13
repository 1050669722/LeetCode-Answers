# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:47:20 2019

@author: Administrator
"""

#class Solution:
#    def minMeetingRooms(self, intervals: list) -> int:
#        if intervals == []:
#            return 0
#        else:
#            result_1 = 1
#            result_2 = 0
#            d = {}
#            intervals = self.merge_sort(intervals)
#            original_intervals = intervals.copy()
##            print(intervals)
#            k = -1
#            for _ in range(len(intervals)-1):
#                k += 1
#                if k == len(intervals)-1:
#                    break
#                if intervals[k][-1] >= intervals[k+1][0]:
##                    result_1 += 1
#                    intervals.insert(k, [intervals[k][0], max(intervals[k][-1], intervals[k+1][-1])])
#                    intervals.pop(k+1)
#                    intervals.pop(k+1)
#                    k -= 1
#            for k in range(len(original_intervals)-1):
#                if original_intervals[k][-1] >= original_intervals[k+1][0]:
#                    result_1 += 1
#            for k in range(len(original_intervals)-1):
#                if original_intervals[k][-1] not in d.keys():
#                    d[original_intervals[k][-1]] = 1
#                else:
#                    d[original_intervals[k][-1]] += 1
##            print(d)
#            for k in range(len(original_intervals)):
#                if (original_intervals[k][0] in d.keys()) and (d[original_intervals[k][0]] > 0):
#                    result_2 += 1
#                    d[original_intervals[k][0]] -= 1 
#            print(result_1)
#            print(result_2)
#            return result_1 - result_2
#        
#    def merge(self, left, right):
#        p, q = 0, 0
#        ans = []
#        while p<len(left) and q<len(right):
#            if left[p][0] <= right[q][0]:
#                ans.append(left[p])
#                p += 1
#            else:
#                ans.append(right[q])
#                q += 1
#        ans += left[p:]
#        ans += right[q:]
#        return ans
#        
#    def merge_sort(self, List):
#        if len(List) <= 1:
#            return List
#        else:
#            num = len(List) // 2
#            left = self.merge_sort(List[num:])
#            right = self.merge_sort(List[:num])
#            return self.merge(left, right)


#class Solution(object): 
#    def minMeetingRooms(self, intervals): 
#        """ :type intervals: List[List[int]] :rtype: int """ 
#        sum_n = 1 
#        if len(intervals) == 0: 
#            return 0 
#        if len(intervals) == 1: 
#            return 1 
#        intervals = sorted(intervals) 
#        times = {1:[[0,0]]} 
#        for interval in intervals: 
#            for key in times.keys(): 
#                if interval[0] >= times[key][-1][1]: 
#                    times[key].append(interval) 
#                    break 
#                else: 
#                    times[len(times)+1] = [interval]


class Solution(object): 
    def minMeetingRooms(self, intervals): 
        """ :type intervals: List[List[int]] :rtype: int """ 
        if not intervals: 
            return 0 
        intervals = sorted(intervals) 
        rooms = [ [intervals[0][1]] ] 
        for interval in intervals[1:]:
#            print(interval[1])
            no_room = 1 
            for room in rooms: 
                if interval[0]>=room[0]: 
                    room[0] = interval[1] 
                    no_room=0 
                    break 
                if no_room: #没有经历过上面那个if
                    rooms.append([interval[1]]) 
                    break
        return len(rooms)

solu = Solution()
intervals = [[0, 30],[5, 10],[15, 20]]
#intervals = [[7,10],[2,4]]
intervals = [[2,11],[6,16],[11,16]]
#intervals = [[13,15],[1,13],[6,9]]
print(solu.minMeetingRooms(intervals))