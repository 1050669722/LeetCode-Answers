# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:41:57 2019

@author: Administrator
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        tmp = 0
        carry = 0
        ans = []
        
        while num1 and num2:
            a = int(num1.pop())
            b = int(num2.pop())
            tmp = a + b + carry
            carry = tmp // 10
            tmp = tmp % 10
            ans.append(str(tmp))
        
        while num1:
            a = int(num1.pop())
            tmp = a + carry
            carry = tmp // 10
            tmp = tmp % 10
            ans.append(str(tmp))
            
        while num2:
            b = int(num2.pop())
            tmp = b + carry
            carry = tmp // 10
            tmp = tmp % 10
            ans.append(str(tmp))
         
        if not num1 and not num2 and carry != 0:
            ans.append(str(carry))    
        
#        print(ans)
        ans.reverse()
        return ''.join(ans)
        
        
        
        
solu = Solution()
num1, num2 = '123', '4567' #4690
num1, num2 = '1', '9'
#num1, num2 = '0', '0'
#num1, num2 = '9', '99'
print(solu.addStrings(num1, num2))