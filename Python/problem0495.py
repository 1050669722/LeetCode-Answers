# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:22:13 2019

@author: Administrator
"""

class Solution:
    def findPoisonedDuration(self, timeSeries: list, duration: int) -> int:
#        Sum = 0
#        for k in range(1, len(timeSeries)):
#            if timeSeries[k] - timeSeries[k-1] >= duration:
#                Sum += duration
#            else:
#                Sum += timeSeries[k] - timeSeries[k-1]
#        return Sum + duration
        
        if not timeSeries:
            return 0
        Sum = 0
        for k in range(1, len(timeSeries)):
            Sum += min(timeSeries[k] - timeSeries[k-1], duration)
        return Sum + duration
        
solu = Solution()
timeSeries, duration = [1,4], 2
#timeSeries, duration = [1,2], 2
print(solu.findPoisonedDuration(timeSeries, duration))