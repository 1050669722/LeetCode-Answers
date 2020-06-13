# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:18:44 2019

@author: Administrator
"""

class Solution:
    def toLowerCase(self, string: str) -> str:
#        return string.lower()
        string = list(string)
        for k in range(len(string)):
            if 'A'<=string[k] and string[k]<='Z':
                temp = ord(string[k])
                temp += 32#chr(ord('1')+3)
                string[k] = chr(temp)
        return ''.join(string)
        
        
        
        
        
solu = Solution()
string = 'Hello'
string = 'here'
string = 'LOVELY'
print(solu.toLowerCase(string))