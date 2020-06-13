# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:36:02 2019

@author: Administrator
"""

class Solution:
    def diStringMatch(self, S: str) -> list:
#        if not S:
#            return []
#        A = list(range(len(S)+1))
#        S = list(S)
#        d = {}
#        print(A)
#        print(S)
#        for k in range(len(A)):
#            d[k] = [k]
#            
##            for p in S:
#        for k in range(len(S)):
#            print(d)
#            if S[k] == 'I':
#                for p in range(len(A)):
#                    for key, value in d.items():
#                        if A[p]>value[-1]:
#                            d[key].append(k)
#            elif S[k] == 'D':
#                for p in range(len(A)):
#                    for key, value in d.items():
#                        if A[p]<value[-1]:
#                            d[key].append(k)
#            print(d)
#        Max = 0
#        mark = 0
#        for k, v in d.items():
#            if len(v)>Max:
#                mark = k
#        return d[mark]
#            
##        for k in S:
##            if k == 'I':
##                A.append(A[-1]+1)
##            elif k == 'D':
##                A.append(A[-1]-1)
##        return A
        
        ans = []
        i = 0
        j = len(S)
        for s in S:
            if s == 'I':
                ans.append(i)
                i += 1
            else:
                ans.append(j)
                j -= 1
        ans.append(i)
        return ans
        
solu = Solution()
S = "IDID"
print(solu.diStringMatch(S))