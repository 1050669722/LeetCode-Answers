# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:11:51 2019

@author: Administrator
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
#        if n == 1:
#            return x
#        if x!=0 and n == 0:
#            return 1
#        if x == 0 and n <= 0:
#            return None
#        if n>0:
#            if n%2 == 0:
#                return self.myPow(x, n//2) * self.myPow(x, n//2)
#            else:
#                return self.myPow(x, n//2) * self.myPow(x, n//2) * x
#        if n<0:
#            if n%2 == 0:
#                return 1. / ( self.myPow(x, -n//2) * self.myPow(x, -n//2) )
#            else:
#                return 1. / ( self.myPow(x, -n//2) * self.myPow(x, -n//2) * x )
        
##        if n == 1:
##            return x
##        if n == 0:
##            return 1
#        if n == 1:
#            return x
#        if x!=0 and n == 0:
#            return 1
#        if x == 0 and n <= 0:
#            return None
#        if n>0:
#            temp = self.myPow(x, n//2)
#            if n%2 == 0:
#                return temp * temp
#            else:
#                return temp * temp * x
#        if n<0:
#            temp = self.myPow(x, -n//2)
#            if n%2 == 0:
#                return 1. / ( temp * temp )
#            else:
#                return 1. / ( temp * temp * x )
        
#        if n == 1: return x
#        if n == 0: return 1
#        t = self.myPow(x, abs(n) // 2)
#        if n % 2 == 0:
#            t = t * t
#        else: t =  x * t * t
#        if n < 0:
#            return 1.0  /t
#        return t
        
        if n<0:
            n = -n
            x = 1. / x
        ans = 1
        cp = x
        while n>=1:
            ans = ans*cp**(n%2)
#            cp **= 2
            cp *= cp
            n //= 2
        return ans
        
solu = Solution()
x, n = 2.00000, 10
#x, n = 2.00000, 4
#x, n = 2.10000, 3
#x, n = 2.00000, -2
#x, n = 0.00001, 2147483647#2**31-1#
#x, n = 0.00000, -1
print(solu.myPow(x, n))