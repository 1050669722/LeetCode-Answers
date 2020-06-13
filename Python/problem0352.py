# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:53:34 2019

@author: Administrator
"""

class SummaryRanges():

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stream = []
        self.List = []

    def addNum(self, val: int) -> None:
        self.stream.append(val)
        self.val = val

    def getIntervals(self) -> list:
        if len(self.stream) == 0:
            return []
        elif len(self.stream) == 1:
            self.List.append([self.stream[0], self.stream[0]])
            return self.List
        else:
            newInterval = [self.val, self.val]
            
            mark = 0
        
            count = 0
            for m in range(len(self.List)):
#                print(m)
#                print(newInterval[0])
#                print(self.List[m][0])
                if newInterval[0] <= self.List[m][0]:
                    mark = m
                    count += 1
                    break
            if count == 0: mark = len(self.List)
            
            self.List.insert(mark, newInterval)    
            
            k = -1
            for _ in range(len(self.List)):
                k += 1
                if k == len(self.List) - 1: break
                if self.List[k][-1] - self.List[k+1][0] >= -1:
                    self.List.insert(k, [self.List[k][0], max(self.List[k][-1],self.List[k+1][-1])])
                    self.List.pop(k+1)
                    self.List.pop(k+1)
                    k -= 1
            return self.List
        
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#class SummaryRanges:
#
#    def __init__(self):
#        """
#        Initialize your data structure here.
#        """
#        self._list = []
#        
#
#    def addNum(self, val: int) -> None:
#        import bisect
#        if val not in self.contain:
#            bisect.insort(self._list, val)
#                
#        
#
#    def getIntervals(self) -> List[Interval]:
#        res = []
#        n = len(self._list)
#        i = 0
#        while i < n:
#            j = i
#            while j < n - 1 and self._list[j]+ 1 == self._list[j+1]:
#                j += 1
#            res.append(Interval(self._list[i], self._list[j]))
#            i = j + 1
#        return res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
        
SR = SummaryRanges()
a = [1,3,7,2,6]
while a:
    val = a.pop(0)
    SR.addNum(val)
    param = SR.getIntervals()
    print(param)        
        
        
        
        