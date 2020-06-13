# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:06:34 2019

@author: Administrator
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
#        if not A and not B:
#            return False
##        if A == B:
##            return False
##        if (A and not B) or (not A and B):
##            return False
#        if len(A) != len(B):
#            return False
#        a = []
#        for k in range(len(A)):
#            if A[k] != B[k]:
#                a.append(k)
##        if len(a) == 0:
##            return True
##        print(len(a))
#        if len(a) != 2 and len(a) != 0:
##            print(-3)
#            return False
#        elif len(a) == 2:
#            A = list(A)
#            A[a[0]], A[a[1]] = A[a[1]], A[a[0]]
#            A = ''.join(A)
#            if A == B:
#                return True
#            else:
##                print(-2)
#                return False
#        else:
##            print(-1)
#            for k in range(1, len(A)):
#                if A[k] != A[k-1]:
#                    return False
#            return True
        
#        if len(A) != len(B): return False
#        if A == B:
#            seen = set()
#            for a in A:
#                if a in seen:
#                    return True
#                seen.add(a)
#            return False
#        else:
#            pairs = []
#            for a, b in itertools.izip(A, B):
#                if a != b:
#                    pairs.append((a, b))
#                if len(pairs) >= 3: return False
#            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
        
        # 长度不同直接false
        if len(A) != len(B): return False
        
        # 由于必须交换一次，在相同的情况下，交换相同的字符
        if A == B and len(set(A)) < len(A): return True
        
        # 使用 zip 进行匹配对比，挑出不同的字符对
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        
        # 对数只能为2，并且对称，如 (a,b)与(b,a)
        return len(dif) == 2 and dif[0] == dif[1][::-1]
        
        
solu = Solution()
A, B = 'ab', 'ba'
A, B = 'ab', 'ab'
A, B = 'aa', 'aa'
#A, B = 'aaaaaaabc', 'aaaaaaacb'
#A, B = '', 'aa'
print(solu.buddyStrings(A, B))