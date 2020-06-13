# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:01:02 2019

@author: Administrator
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
#        self.MIN = None

    def push(self, x: int) -> None:
        self.a.append(x)
#        try:
#            if x < self.MIN:
#                self.MIN = x
#        except:
#            self.MIN = x

    def pop(self) -> None:
        self.a.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return min(self.a)#self.MIN


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()