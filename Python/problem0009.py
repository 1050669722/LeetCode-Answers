# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:15:12 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

#class Solution():
#    def isPalindrome(self, x):
#        a = [i for i in str(x)]
#        if a == list(reversed(a)):
#            return True
#        else:
#            return False

#class Solution():
#    def isPalindrome(self, x):
#        if x<0 or (x % 10 == 0 and x != 0):
#            return False
#        else:
#            ReverseNumber = 0
#            while(x > ReverseNumber):
#                ReverseNumber = ReverseNumber * 10 + x % 10
#                x //= 10
#            return x == ReverseNumber or x == ReverseNumber // 10 

class Solution():
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        else:
            R = 0
            while(x > R):
                R = R * 10 + x % 10
                x //= 10
            return x == R or x == R // 10

solu = Solution()
x = 121
x = -121
x = 10
print(solu.isPalindrome(x))

time2 = time.perf_counter()
print(time2-time1)












