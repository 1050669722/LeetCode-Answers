# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:47:40 2019

@author: Administrator
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        elif num > 0:
            ans = []
            while num > 0:
                tmp = num % 7
                num //= 7
                ans.append(str(tmp))
            ans.reverse()
            return ''.join(ans)
        else:
            ans = []
            num *= -1
            while num > 0:
                tmp = num % 7
                num //= 7
                ans.append(str(tmp))
            ans.append('-')
            ans.reverse()
            return ''.join(ans)
            
#class Solution:
#    def convertToBase7(self, num: int) -> str:
#        if num == 0:
#            return "0"
#        flag = 1 if num > 0 else -1
#        res = ""
#        while num != 0:
#            res = str(abs(num) % 7) + res #可以这样拼接字符串
#            num = abs(num) // 7
#        return res if flag == 1 else '-'+res
        
        
solu = Solution()
num = 100
num = -7
num = 0
print(solu.convertToBase7(num))