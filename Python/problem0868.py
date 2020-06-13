# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:11:43 2019

@author: ASUS
"""

class Solution:
    def binaryGap(self, N: int) -> int:
        a = []
        while N:
            a.append(N % 2)
            N //= 2
        idx = []
        count = 0
        while a:
            if a.pop():
                idx.append(count)
            count += 1
        res = []
        for k in range(1, len(idx)):
            res.append(idx[k]-idx[k-1])
        if not res:
            return 0
        return max(res)
    
#class Solution(object):
#def binaryGap(self, N):
#    A = [i for i in xrange(32) if (N >> i) & 1]
#    if len(A) < 2: return 0
#    return max(A[i+1] - A[i] for i in xrange(len(A) - 1))
#
##作者：LeetCode
##链接：https://leetcode-cn.com/problems/two-sum/solution/er-jin-zhi-jian-ju-by-leetcode/
##来源：力扣（LeetCode）
##著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            
            
        
solu = Solution()
N = 22
#N = 5
#N = 6
#N = 8
print(solu.binaryGap(N))