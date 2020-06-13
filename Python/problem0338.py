# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:01:01 2019

@author: Administrator
"""

class Solution:
    def countBits(self, num: int) -> list:
#        p = 0
#        while 2**p < num:
#            p += 1
#        a = [0]
#        for _ in range(p+1):
#            a += [x+1 for x in a]
#        ans = []
#        for k in range(num+1):
#            ans.append(a[k])
#        return ans
        
        target = [0]
        count1 = 1 
        count2 = 1
        for i in range(1,num+1):
            if count2 == 0:
                count1 *= 2 #c1是一种距离
                count2 = count1-1 #c2是用来计数的，c2减到0的时候，c1就乘2
                target.append(target[i-count1]+1)
            else:
                target.append(target[i-count1]+1)
                count2 -= 1
        return target

#作者：pandawakaka
#链接：https://leetcode-cn.com/problems/two-sum/solution/python3nei-zhi-han-shu-fang-fa-by-pandawakaka/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            
solu = Solution()
num = 2
#num = 5
print(solu.countBits(num))