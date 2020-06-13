# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:36:38 2019

@author: Administrator
"""

class Solution:
    def countPrimes(self, n: int) -> int:
#      if n<=2:
#          return 0
##      if n==3:
##          return 1
#      count = 0
#      for k in range(2, n):
#          if k == 2:
#              count += 1
#              continue
#          mark = 0
#          for p in range(2, k):
#              if k % p == 0:
#                  mark += 1
##                  print(k,p)
##                  break
#          if mark == 0:
#              count += 1
#      return count
        
#        a = list(range(2, n))
#        for k in range(len(a)):
#            for p in range(k+1, len(a)):
#                if a[p] % a[k] == 0:
#                    del a[p]
        
    #     if n <= 2:
    #         return 0
    #     count = 0
    #     for num in range(2, n):
    #         count += self.isPrime(num)
    #     return count
    # def isPrime(self, num):
    #     for k in range(2, num):
    #         if num % k == 0:
    #             return 0
    #     return 1

        # if n <= 2:
        #     return 0
        # List = list(range(2, n))
        # tmp = []
        # for p in range(len(List)):
        #     for q in range(p+1, len(List)):
        #         if List[q] % List[p] == 0: #如果List[q]能整除List[p]
        #             tmp.append(List[q])
        # return len( set(List) - set(tmp) ) #sorted( list( set(List) - set(tmp) ) )

        # isPrimes = [1] * n
        # res = 0
        # for i in range(2, n):
        #     if isPrimes[i] == 1: res += 1
        #     j = i
        #     while i * j < n:
        #         isPrimes[i * j] = 0
        #         j += 1
        # return res

        # if n < 2: return 0
        # isPrimes = [1] * n
        # isPrimes[0] = isPrimes[1] = 0
        # for i in range(2, int(n ** 0.5) + 1):
        #     if isPrimes[i] == 1:
        #         isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        # return sum(isPrimes)

        if n < 2:
            return 0
        P = [1] * n
        P[0] = P[1] = 0 #0和1不是质数
        for k in range(2, n): #k就表示某一个数 #根据下面的切片形式，当k大于n的平方根时，就没有那个切片了；这个时候P数组也已经做好了
            if P[k] == 1:
                P[k**2:n:k] = [0] * len(P[k**2:n:k])
        return sum(P)

solu = Solution()
# n = 10
#n = 3
#n = 4
n = 10000
# n = 499979
print(solu.countPrimes(n))