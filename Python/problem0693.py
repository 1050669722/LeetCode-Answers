# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:51:28 2019

@author: ASUS
"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
#        a = []
#        while n:
#            tmp = n % 2
#            a.append(tmp)
#            if len(a) >=2 and a[-1] == a[-2]:
#                return False
#            n //= 2
#        return True
        
        a = [0] * 2
        count = 0
        while n:
            tmp = n % 2
            n //= 2
            a[count%2] = tmp
            count += 1
            if count>=2 and a[0] == a[1]:
                return False
        return True
        
        
solu = Solution()
n = 5
n = 7
n = 11
#n = 10
print(solu.hasAlternatingBits(n))