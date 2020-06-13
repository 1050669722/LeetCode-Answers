# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:24:13 2019

@author: Administrator
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0#ans = []#
        for k in range(len(s)):
            m = 0
            while 0<=k-m and k+m<=len(s)-1 and s[k-m] == s[k+m]:
                count += 1#ans.append(s[k-m:k+m+1])#
                m += 1
        for p in range(len(s)-1):
            q = p+1
            m = 0
            if s[p]==s[q]:
                while 0<=p-m and q+m<=len(s)-1 and s[p-m] == s[q+m]:
                    count += 1#ans.append(s[p-m:q+m+1])#
                    m += 1
#            while s[p]==s[q] and 0<=p-m and q+m<=len(s)-1 and s[p-m] == s[q+m]:
#                ans.append(s[p-m:q+m+1])
#                m += 1
        return count#len(ans)#
        
        
        
        
        
solu = Solution()
s = "abc"
s = "aaa"
print(solu.countSubstrings(s))