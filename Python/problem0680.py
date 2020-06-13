# -*- coding: utf-8 -*-
"""
Created on Sat May 25 13:59:24 2019

@author: Administrator
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
#        p = 0
#        q = len(s) - 1
#        mark = 0
#        while p < q:
#            if s[p] != s[q]:
#                mark += 1
##                q -= 1
##                print(mark)
##                print(s[p],s[q-1])
##                print(s[p+1],s[q])
#                if mark != 1 or (s[p] != s[q-1] and s[p+1] != s[q]):
#                    return False
#                if s[p] == s[q-1]:
#                    print(-1)
#                    q -= 1
##                if s[p+1] == s[q] and s[p] != s[q-1]:
#                elif s[p+1] == s[q]:
#                    print(-2)
#                    p += 1
##            print(p,q)
#            p += 1
#            q -= 1
#        return True
        
        return (self.judge1(s) or self.judge2(s))
        
    def judge1(self, s):
        p = 0
        q = len(s) - 1
        mark = 0
        while p < q:
            if s[p] != s[q]:
                mark += 1
                if mark != 1 or (s[p] != s[q-1] and s[p+1] != s[q]):
                    return False
                q -= 1
            p += 1
            q -= 1
        return True
    
    def judge2(self, s):
        p = 0
        q = len(s) - 1
        mark = 0
        while p < q:
            if s[p] != s[q]:
                mark += 1
                if mark != 1 or (s[p] != s[q-1] and s[p+1] != s[q]):
                    return False
                p += 1
            p += 1
            q -= 1
        return True
        
solu = Solution()
s = "aba"
#s = "abca"
#s = 'abba'
#s = 'aaabssbcaaa'
#s = "deeee"
#s = 'e'
#s = "cdbeeeabddddbaeedebdc"
s = "ebcbbececabbacecbbcbe"
print(solu.validPalindrome(s))








