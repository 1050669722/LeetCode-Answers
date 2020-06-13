# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:47:38 2019

@author: ASUS
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for k in range(1, 26+1):
            d[chr(ord('A')-1+k)] = k
        s = list(s)
        ans = 0
        count = 0
        while s:
            ans += d[s.pop()] * 26**count
            count += 1
        return ans
        
solu = Solution()
s = 'A'
#s = 'AB'
#s = 'ZY'
print(solu.titleToNumber(s))