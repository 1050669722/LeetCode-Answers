# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:28:03 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

#class Solution:
#    def plusOne(self, digits):
#        a = [str(i) for i in digits]
#        a = int(''.join(a))
#        a += 1
#        a = [i for i in str(a)]
#        a = [int(i) for i in a]
#        return a

#class Solution():
#    def plusOne(self, digits):
#        '''由个位开始处理
#        '''
#        is_carry = 1 #进位标记，假定题目的+1是由低位进上来的，初始设为1
#        result = []
#        for d in digits[::-1]: #digits[::-1]遍历整个列表，步长为-1
#            d = d + is_carry
#            is_carry = d//10
#            result.append(d%10)
#            # d = d % 10
#        if is_carry: # 再判断一下是否需要继续进位
#            result.append(1)
#        return result[::-1]

class Solution():
    def plusOne(self, digits):
        ans = []
        carry = 1
        for d in digits[::-1]:
            d += carry
            ans.append(d % 10)
            carry = d // 10
        if carry:# == 1:
            ans.append(1)
        return ans[::-1]
    
solu = Solution()
a = [1,2,3]
print(solu.plusOne(a))

time2 = time.perf_counter()
print(time2 - time1)






