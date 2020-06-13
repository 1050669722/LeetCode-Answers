# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:34:57 2019

@author: Administrator
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
#        a = []
#        for k in s:
#            if ('a'<=k.lower() and k.lower()<='z') or ('0'<=k and k<='9'):
#                a.append(k.lower())
##        print(a)
#        return a == a[::-1]
        p = 0
        q = len(s) - 1
        while p < q: #循环套循环也不一定增加了时间复杂度
            while (p < q) and (not(('a'<=s[p].lower() and s[p].lower()<='z') or ('0'<=s[p] and s[p]<='9'))):
                p += 1
            while (p < q) and (not(('a'<=s[q].lower() and s[q].lower()<='z') or ('0'<=s[q] and s[q]<='9'))):
                q -= 1
#            print(s[p], s[q])
            if s[p].lower() != s[q].lower():
                return False
            p += 1
            q -= 1
        return True

        
        
        
solu = Solution()
s = "A man, a plan, a canal: Panama"
s = "race a car"
s = "`l;`` 1o1 ??;l`"
print(solu.isPalindrome(s))