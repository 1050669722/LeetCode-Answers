# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:18:35 2019

@author: ASUS
"""

class Solution:
    def singleNumber(self, nums: list) -> list:
#        from collections import defaultdict
#        d = defaultdict(int)
#        ans = []
#        for num in nums:
#            d[num] += 1
#        for num in nums:
#            if d[num] == 1:
#                ans.append(num)
#        return ans
        
#        d = {}.fromkeys(nums, 0)
#        ans = []
#        for num in nums:
#            d[num] += 1
#        for num in nums:
#            if d[num] == 1:
#                ans.append(num)
#        return ans
        
        tmp = 0
        for num in nums:
            tmp ^= num
        print(tmp)
        t = 0
        count = 0
        while tmp:
            t += (tmp % 2) * 10**count
            count += 1
            tmp //= 2
        return t
    
solu = Solution()
nums = [1,2,1,3,2,5]
print(solu.singleNumber(nums))