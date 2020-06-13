# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:35:51 2019

@author: Administrator
"""

class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
#        if s == []:
#            return None
#        else:
#            length = len(s)
#            for k in range(len(s)-1, -1, -1):
#                s.append(s[k])
##            s = s[length+1:]
#            for _ in range(length):
#                s.pop(0)
#            return None
#        if s == []:
#            return None
#        else:
#            length = len(s)
#            for k in range(len(s)-1, -1, -1):
#                s.append(s[k])
##            s = s[length+1:]
##            for _ in range(length):
##                s.pop(0)
##            return None
#            del s[:length]
        
#class Solution:
#    def reverseString(self, s: List[str]) -> None:
#        length = len(s)
#        for i in range(length//2):
#            s[i],s[length-i-1] = s[length-i-1],s[i]
            
        for k in range(len(s)//2):
            s[0+k], s[len(s)-1-k] = s[len(s)-1-k], s[0+k]
        
solu = Solution()
s = ["h","e","l","l","o"]
#s = ["H","a","n","n","a","h"]
#s = []
solu.reverseString(s)
print(s)