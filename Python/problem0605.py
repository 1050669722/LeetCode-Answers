# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:59:05 2019

@author: Administrator
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
#        if 1 not in flowerbed:
#            if len(flowerbed)%2 == 0:
#                return n <= len(flowerbed) // 2
#            else:
#                return n <= len(flowerbed) // 2 + 1
#        elif len(flowerbed) <= 2:
#            return n == 0
#        elif [0 for _ in range(len(flowerbed)-1)] == flowerbed[:-1] and flowerbed[-1] == 1:
#            return n <= self.fun2(len(flowerbed))
#        else:
#            Sum = 0
#            p, q = 0, 0
#            while p<=q:
#                if q == len(flowerbed)-1:
##                    print(q)
#                    if flowerbed[q] == 1:
##                        print(p,q)
#                        Sum += self.fun1(q-p+1)
#                    else:
#                        Sum += self.fun2(q-p+1)
#                    break
#                if flowerbed[q] != 0:
#                    if flowerbed[p] == 1:
#                        Sum += self.fun1(q-p+1)
#                    else:
#                        Sum += self.fun2(q-p+1)
#                    p = q
#                q += 1
#        return n <= Sum
#                
#    def fun1(self, length):
#        if length <= 2:
#            return 0
#        if (length-2)%2 != 0:
#            return ((length-2)+1)//2-1
#        else:
#            return ((length-2))//2-1
#        
#    def fun2(self, length):
#        if (length)%2 != 0:
#            return ((length)+1)//2-1
#        else:
#            return ((length))//2-1
        
        k = 0
        while k < len(flowerbed) and n>0:
            if flowerbed[k] == 0 and (k == 0 or flowerbed[k-1] == 0) and (k == len(flowerbed)-1 or flowerbed[k+1] == 0):#在or这里有短路效应
#            if flowerbed[k] == 0 and (flowerbed[k-1] == 0 or k == 0) and (flowerbed[k+1] == 0 or k == len(flowerbed)-1):
                n -= 1
                k += 2#1#
            else:
                k += 1
        return n == 0
                
solu = Solution()
flowerbed, n = [1,0,0,0,1], 1
flowerbed, n = [1,0,0,0,1], 2
#flowerbed, n = [0,0,0,1], 1
flowerbed, n = [0, 0], 2
flowerbed, n = [1,0,0,0,1,0,0], 2
print(solu.canPlaceFlowers(flowerbed, n))