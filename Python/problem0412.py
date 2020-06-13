# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:29:55 2019

@author: ASUS
"""

class Solution:
    def fizzBuzz(self, n: int) -> list:
        ans = []
        for num in range(1, n+1):
            ans.append(self.output(num))
        return ans
    def output(self, num):
        s = []
        if num % 3 == 0:
            s.append('Fizz')
        if num % 5 == 0:
            s.append('Buzz')
        if not s:
            s.append(str(num))
        return ''.join(s)
        
        
solu = Solution()
n = 15
print(solu.fizzBuzz(n))