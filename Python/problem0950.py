# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:08:46 2019

@author: Administrator
"""

class Solution:
    def deckRevealedIncreasing(self, deck: list) -> list:
        deck.sort()
        n = len(deck)
        ans = [deck[-1]]
        deck.pop()
#        print(ans)
#        print(deck)
        while len(ans) < n:
            ans.insert(0, deck.pop())
            if len(ans) == n:
                break
            ans.insert(0, ans.pop())
#            ans.insert(0, ans[-1])
#            ans.pop()
#            print(ans)
            
        return ans
        
solu = Solution()
deck = [17,13,11,2,3,5,7]
print(solu.deckRevealedIncreasing(deck))