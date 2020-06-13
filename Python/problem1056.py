# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:22:05 2019

@author: ASUS
"""

class Solution:
    def confusingNumber(self, N: int) -> bool:
#        from collections import defaultdict
#        d = defaultdict(int)
#        a = []
#        n = N
#        while n:
#            tmp = n % 10
#            a.append(tmp)
#            n //= 10
#        for k in a:
#            if k in [0, 1, 9, 8, 6]:
#                if k in [6, 9] :
#                    d[k] = 1
#                else:
#                    d[k] = 0
#            else:
#                 d[k] = -1       
#        a.reverse()
#        print(a)
#        print(d)
#        count = 0
#        while N:
#            tmp = N % 10
#            if d[tmp] == -1:
#                return False
#            elif d[tmp] == 1:
#                count += 1
#            N //= 10
#        if count > 0:
#            return True
#        else:
#            return False
        
        a = []
        n = N
        while n:
            tmp = n % 10
            a.append(tmp)
            n //= 10
        for k in range(len(a)):
            if a[k] in [0, 1, 9, 8, 6]:
                if a[k] == 6:
                    a[k] = 9
                elif a[k] == 9:
                    a[k] = 6
            else:
                 return False
#        a = [str(x) for x in a]
#        a = ''.join(a)
#        a = int(a)
#        return a != N
        b = 0
        for k in range(len(a)):
            tmp = a.pop() * 10**k
            b += tmp
        return b != N
        
solu = Solution()
N = 6
N = 89
N = 11
N = 25
N = 916
print(solu.confusingNumber(N))