# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:14:25 2019

@author: ASUS
"""

class Solution:
    def sumOfDigits(self, A: list) -> int:
#        A.sort()
#        num = A[0]
#        num = min(A)
        A = self.merge_sort(A)
        num = A[0]
        S = 0
        while num:
            S += num % 10
            num //= 10
        return int(S % 2 == 0)
    
    def merge(self, left, right):
        p, q = 0, 0
        ans = []
        while p<len(left) and q<len(right):
            if left[p] <= right[q]:
                ans.append(left[p])
                p += 1
            else:
                ans.append(right[q])
                q += 1
        ans += left[p:]
        ans += right[q:]
        return ans
        
    def merge_sort(self, List):
        if len(List) <= 1:
            return List
        num = len(List) // 2
        left = self.merge_sort(List[:num])
        right = self.merge_sort(List[num:])
        return self.merge(left, right)
        
solu = Solution()
A = [34,23,1,24,75,33,54,8]
A = [99,77,33,66,55]
print(solu.sumOfDigits(A))



