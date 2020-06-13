# -*- coding: utf-8 -*-
"""
Created on Thu May 23 17:26:52 2019

@author: Administrator
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        head = 0
        tail = x
        mid = (head + tail) // 2
#        a = list(range(head, tail))
        while head < tail:
            if mid**2 < x:
                head = mid + 1
                mid = (head + tail) // 2
            elif mid**2 > x:
                tail = mid - 1
                mid = (head + tail) // 2
            else:
                return mid
#        print(head-1)
#        print(tail+1)
#        print(mid)
        head -= 1
        tail += 1
#        if abs(head**2-x) == min(abs(head**2-x), abs(tail**2-x), abs(mid**2-x)):
#            return head
#        elif abs(tail**2-x) == min(abs(head**2-x), abs(tail**2-x), abs(mid**2-x)):
#            return tail
#        else:
#            return mid
        smallest = abs(head**2-x)
        mark = 0
        count = -1
        a = [head, tail, mid]
        # print(a)
        # print('******')
        for k in [head**2, tail**2, mid**2]:
            count += 1
            if k <= x and abs(k-x) <= smallest: #不超过，差距又最小
#                print(count)
                smallest = abs(k-x)
                mark = count #这个count是一个索引的作用
            else:
                pass
        # print(a)
        return a[mark]

solu = Solution()
x = 4
#x = 2
# x = 8
print(solu.mySqrt(x))