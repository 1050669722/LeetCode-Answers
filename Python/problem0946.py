from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        d = {}
        for k, val in enumerate(pushed):
            # pushed[k] = val, k
            d[val] = k
        
        t = {}
        for val in popped:
            if val in t:
                t[val].append(val)
            else:
                
