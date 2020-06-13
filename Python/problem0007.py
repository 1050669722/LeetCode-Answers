# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:52:44 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

#class Solution():
#    def reverse(self, x):
#        a = [i for i in str(x)]
#        a.reverse()
#        for k in range(len(a)):
#            if a[k] != '0':
#                if a[-1] == '-':
#                    a = a[k:-1]
#                    a.insert(0,'-')
#                    if int(''.join(a)) < (-2)**31 or int(''.join(a)) > 2**31-1:
#                        return 0
#                    else:
#                        return int(''.join(a))
#                elif int(''.join(a[k:])) < (-2)**31 or int(''.join(a[k:])) > 2**31-1:
#                    return 0
#                else:
#                    return int(''.join(a[k:]))
#        return x#还有一种情况应该在这里考虑
    
#class Solution():
#    def reverse(self, x: int) -> int:
#        p = -1 if x<0 else 1
#        x = p * x
#        x = list(str(x)) #[i for i in str(x)]
#        x.reverse()
#        x = int(''.join(x))
#        x = p * x
#        if x< -2 ** 31 or x>2**31 - 1:
#            return 0
#        return x

class Solution():
    def reverse(self, x):
        p = -1 if x<0 else 1
        x *= p #符号先隐去
        x = [i for i in str(x)] # list(str(x))
        x.reverse()
        x = p * int(''.join(x)) #符号再出现 #数字字符串可以用int()强制转换，但是列表不可以
        if x > -2**(31) and x < 2**31-1:
            return x
        return 0
    
#x = 123
#x = -123
x = 120
#x = 0
#x = 1534236469
solu = Solution()
print(solu.reverse(x))

time2 = time.perf_counter()
print(time2-time1)






