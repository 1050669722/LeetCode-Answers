# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:17:26 2019

@author: Administrator
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
#        ans = []
#        for num in n:
#            res = 1
#            for k in range(1, num+1):
#                res = res * k
#            tmp = 0    
#            while res%10 == 0:
#                tmp += 1
#                res //= 10
#            ans.append(tmp)
#        return ans
        
#        ans = 0
#        while n:
#            ans += n//5
#            n //= 5
#        return ans
        
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans
        
solu = Solution()
n = 3
n = 5
n = 10
n = 30
n = 200
#n = 100
#n = [200]
#n = [100]
#n = 10000
#n = list(range(0,1000+1))
#n = list(range(0,200+1))
print(solu.trailingZeroes(n))