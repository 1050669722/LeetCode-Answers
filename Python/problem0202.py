# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:55:21 2019

@author: Administrator
"""

class Solution:
    def isHappy(self, n: int) -> bool:
#        while n != 1:
#            a = n
#            temp = 0
#            while a != 0:
#                temp += (a % 10) ** 2
#                a //= 10
#            n = temp
##            if n == 1:
#        return True
        
        d = {0:1, 16:1, 37:1, 58:1, 89:1, 145:1, 42:1, 20:1, 4:1}
        while n != 1:
            try:
                if d[n]:
                    return False
            except:
                pass
            res = 0
            while n:
                tmp = n % 10
                tmp **= 2
                res += tmp
                n //= 10
            n = res
        return True
    
#        for n in range(10, 31):
#            print('---', n ,'---')
#            while n != 1:
#                print(n)
#                res = 0
#                while n:
#                    tmp = n % 10
#                    tmp **= 2
#                    res += tmp
#                    n //= 10
#                n = res
#        return True
        
'''
16
37
58
89
145
42
20
4
'''
        
solu = Solution()
n = 19
n = 0
print(solu.isHappy(n))