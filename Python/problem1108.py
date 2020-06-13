# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:47:39 2019

@author: ASUS
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
#        while '.' in address:
#            address.replace('.','[.]')
#        return adress
        
#        return address.replace('.','[.]')
        
        stack = []
        for k in address:
            if k != '.':
                stack.append(k)
            else:
                stack.append('[')
                stack.append(k)
                stack.append(']')
        return ''.join(stack)
        
solu = Solution()
address = "1.1.1.1"
#address = "255.100.50.0"
print(solu.defangIPaddr(address))