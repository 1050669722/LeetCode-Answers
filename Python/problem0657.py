# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:39:20 2019

@author: ASUS
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
#        stack = []
#        for move in moves:
#            stack.append(move)
#            if len(stack) > 1 and (stack[-2:] == ['U','D'] or stack[-2:] == ['D','U'] or stack[-2:] == ['L','R'] or stack[-2:] == ['R','L']):
#                stack.pop()
#                stack.pop()
#        print(stack)
#        return not stack     

        count = {'L':0, 'R':0, 'U':0, 'D':0}
        for move in moves:
            count[move] += 1
        return count['L'] == count['R'] and count['U'] == count['D']
        
        
solu = Solution()
moves = "UD"
#moves = 'LL'
#moves = "RLUURDDDLU"
print(solu.judgeCircle(moves))