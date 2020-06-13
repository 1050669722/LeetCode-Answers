# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:51:52 2019

@author: ASUS
"""

class Solution:
    def reverseWords(self, s: str) -> str:
#        from collections import deque
#        s = deque(s)
        s = list(s)
#        s.reverse()
        stack = []
        ans = []
        while s:
            tmp = s.pop()
            if tmp != ' ':
                stack.append(tmp)
            else:
                ans.append(''.join(stack))
                stack = []
        ans.append(''.join(stack))
        ans.reverse()
        return ' '.join(ans)
        
        
solu = Solution()
s = "Let's take LeetCode contest"
print(solu.reverseWords(s))