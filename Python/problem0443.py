# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:14:04 2019

@author: Administrator
"""

class Solution:
    def compress(self, chars: list) -> int:
#        count = 1
#        for k in range(len(chars))[len(chars)-2::-1]:
#            if chars[k] == chars[k+1]:
#                count += 1
#                chars.pop()
        
        length = len(chars)
        if length <= 1:
            return length#chars#
        count = 1
#        for k in range(1, len(chars)):
        k = 1
        while k < length:
            if chars[k] == chars[k-1]:
                count += 1
                del chars[k]
            elif count != 1:
                tmp = list(str(count))
                mark = 0
                while tmp:
                    chars.insert(k, tmp.pop())
                    mark += 1
                for _ in range(mark+1):
                    k += 1    
                count = 1
            else:
                k += 1
                
            length = len(chars)
            
        if count != 1:
            tmp = list(str(count))
            while tmp:
                chars.append(tmp.pop(0))
            
        return len(chars)#chars#
                
                
solu = Solution()
#chars = ["a","a","b","b","c","c","c"]
#chars = ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(solu.compress(chars))