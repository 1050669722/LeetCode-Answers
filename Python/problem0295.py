# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:56:01 2019

@author: Administrator
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        if self.data == []:
            return []
        self.data = sorted(self.data)
        if len(self.data) % 2 == 0:
            return ( (self.data[int(len(self.data)/2-1)]) + (self.data[int(len(self.data)/2)]) ) / 2.
        else:
            return self.data[len(self.data)//2]

MF = MedianFinder()
nums = [2,3,4]
#nums = [2,3]
while nums:
    MF.addNum(nums.pop(0))
    print(MF.findMedian())
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()