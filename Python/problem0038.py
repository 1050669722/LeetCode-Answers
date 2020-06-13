# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:46:15 2019

@author: Administrator
"""

#class Solution():
#    def countAndSay(self, n: int) -> str:
##        print(1)
#        if n == 1:
#            return str(n)
#        else:
#            p = 0
#            q = 0
#            target = self.countAndSay(n-1)
#            val = int(target[0])
#            a = []
##            print(target)
##            print(val)
#            for _ in range(1, len(target)):
#                q += 1
#                if (target[q]) != (target[p]):
#                    length = q - p
#                    a.append(length)
#                    a.append(val)
#                    p = q
#                    val = int(target[q])
##            print(q)
##            print(p)
#            a.append(q+1 - p)
#            a.append(val)
#            a = ''.join([str(i) for i in a])
##            print(':'+a)
#            return a
        
class Solution():
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(n)
        else:
            p = 0
            q = 0
            target = self.countAndSay(n-1)
            val = int(target[0])
            a = []
            for _ in range(1, len(target)):
                q += 1
                if (target[q]) != (target[p]):
                    length = q - p
                    a.append(length)
                    a.append(val)
                    p = q
                    val = int(target[q])
            a.append(q + 1 - p)
            a.append(val)
            a = ''.join([str(i) for i in a])
            return a
        
solu = Solution()
#n = 1
#n = 2
#n = 3
#n = 4
#n = 5
#n = 10
n = 30
#solu.countAndSay(n)
print(solu.countAndSay(n))


