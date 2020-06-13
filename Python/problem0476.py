# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:35:24 2019

@author: ASUS
"""

#class Solution:
#    def findComplement(self, num: int) -> int:
#        ans = 0
#        count = 0
#        while num:
#            tmp = num%2
#            tmp = 1 - tmp
#            ans += tmp * 2**count
#            count += 1
#            num //= 2
#        return ans
        
class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        # 最高位为1，其余为0，刚好比num大然后用这个数减去1就是我们要找的数
        while num >= i: 
            i = i << 1 # 每次向左移1位 i=0b1000
        return i-1-num

#作者：wang-hao-bi0glUtbvU
#链接：https://leetcode-cn.com/problems/two-sum/solution/ren-sheng-ku-duan-wo-yong-python3-by-wang-hao-bi0g/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

solu = Solution()
num = 5
#num = 1
print(solu.findComplement(num))