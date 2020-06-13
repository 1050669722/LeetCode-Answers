# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:20:33 2019

@author: Administrator
"""

class Solution:
    def countDigitOne(self, n: int) -> int:
#        count = 0
#        for k in range(1, n+1):
#            for p in list(str(k)):
#                if p == '1':
#                    count += 1
#        return count

        
#        count = 0
#        while n > 9:
#            m = len(str(n)) - 1
#            tmp = 10**m - 1
##            print(tmp)
##            print(self.fun(tmp))
#            count += self.fun(tmp)
#            n -= tmp
#        return count + 1
        
#        tmp = n
#        n = 10 ** (len(str(n)) - 1) - 1
#        tmp -= n
#        count = 0
#        while n:
#            count += self.fun(n)
#            n //= 10
#        return count
#    
#    def fun(self, n):
#        tmp = 0
#        count = 1
#        m = len(str(n))
#        for k in range(1, m):
#            tmp += count
#            count = tmp * 9 + 10 ** k
#        return count
        
#        count = 0
#        
#        if n == 10**len(str(n))-1:
#            while n:
#                count += self.fun(n)
#                n //= 10
#            return count
#        
#        count += self.countDigitOne( 10 ** (len(str(n))-1)-1 )
#        
#        tmp = n - 10 ** ( len(str(n))-1 )
#        count += self.countDigitOne( tmp )
#        
#        count += tmp + 1
#        
##        tmp = n
##        n = 10 ** (len(str(n)) - 1) - 1
##        tmp -= n
##        count = 0
##        while n:
##            count += self.fun(n)
##            n //= 10
##        return count
#    
#    def fun(self, n):
#        tmp = 0
#        count = 1
#        m = len(str(n))
#        for k in range(1, m):
#            tmp += count
#            count = tmp * 9 + 10 ** k
#        return count
        
        
        if n <= 0: #特殊情况
            return 0
        
        if n <= 9:
            return 1
        
        count = 0
        
        if n == 10**len(str(n))-1: #只含9
            while n:
                count += self.fun(n)
                n //= 10
            return count
        
#        while :
#            count += self.countDigitOne(10**(len(str(n))-1)-1)
#            n = n - 10**(len(str(n))-1)
#            if n <= 10**(len(str(n))-1):
#                count += n+1#min(10**(len(str(n))-1), n+1)#
#                count += self.countDigitOne(n)
#            else:
##                count += 10**(len(str(n))-1)#min(10**(len(str(n))-1), n+1)#
#                tmp = int(''.join(list(str(n))[1:]))
#                count += self.countDigitOne(tmp)
#            
#            while :
#                if n >  10**(len(str(n)-1)-1):
            
        count = 0
        m = int(list(str(n))[0]) #直接看最高位是几 #有3个部分可能含有1
        for k in range(m):
            count += self.countDigitOne( 10**(len(str(n))-1)-1 ) #=1=
#            print(k, self.countDigitOne( 10**(len(str(n))-1)-1 ))
        if m == 1: #=2=
            tmp = ''.join(list(str(n))[1:])
            print(tmp, type(tmp))
            count += int(tmp) + 1
        else:
            count += 10 ** (len(str(n))-1)
#        print(10 ** (len(str(n))-1))
        tmp = ''.join(list(str(n))[1:])
#        print(tmp, type(str(tmp)))
        count += self.countDigitOne( int(tmp) ) #=3=
#        print(count)
        return count
        
    def fun(self, n): #找规律
        tmp = 0
        count = 1
        m = len(str(n))
        for k in range(1, m):
            tmp += count
            count = tmp * 9 + 10 ** k
        return count
        
        
solu = Solution()
#n = 13
#n = 3184191
n = 9999
#n = 1000
#n = 9
n = 1024
n = 999
n = 1999
n = 1789
#n = 2789
n = 2
n = 20
#n = 21
n = -1
print(solu.countDigitOne(n))
#print(solu.fun(7))


class Solution(object):
    def countDigitOne(self, n):
        """
       用递归做的，可以改成记忆化搜索，加快时间
        """
        if n<=0: return 0
        if n<10: return 1
        last = int(str(n)[1:])
        power =  10**(len(str(n))-1)      
        high = int(str(n)[0])
        if high == 1:
            return self.countDigitOne(last) + self.countDigitOne(power-1) + last+1
        else:
            return self.countDigitOne(last) + high*self.countDigitOne(power-1) + power