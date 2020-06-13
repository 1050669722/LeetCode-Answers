# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:50:56 2019

@author: Administrator
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
#        while a&b != 0:
#            m = a
#            n = b
#            a = m^n
#            b = int(m&n)#<<1
#        return a^b
        
        m = a ^ b
        n = (a & b)<<1
        while(n):
            m_temp = m
            n_temp = n
            m = m_temp ^ n_temp
            n = (m_temp & n_temp)<<1
        return m
        
        
        
        
        
solu = Solution()
a, b = 1, 2
a, b = -2, 3
print(solu.getSum(a,b))