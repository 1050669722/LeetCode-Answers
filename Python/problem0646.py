# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:48:54 2019

@author: Administrator
"""

class Solution:
    def findLongestChain(self, pairs: list) -> int:
#        pairs = sorted(pairs, key = lambda x: x[1], reverse = False)
##        print(pairs)
#        d = {}
#        for p in range(len(pairs)):
#            d[p] = []
#            d[p].append(pairs[p])
#            for k in d.keys():
#                if d[k][-1][-1] < pairs[p][0]:
#                    d[k].append(pairs[p])
#        print(d)
#        Max = 0
#        for k, v in d.items():
##            if len(v) > Max:
##                Max = len(v)
#            Max = max(Max, len(v))
#        return Max
        
#        pairs = sorted(pairs, key = lambda x: x[0])
##        print(pairs)
#        d = {}
#        for p in range(len(pairs))[::-1]:
#            d[p] = []
#            print(pairs[p])
#            d[p].append(pairs[p])
#            for k in d.keys():
#                print(d[k][-1][0], pairs[p][-1])
#                if d[k][-1][0] > pairs[p][-1]:
#                    d[k].append(pairs[p])
#        print(d)
#        Max = 0
#        for k, v in d.items():
##            if len(v) > Max:
##                Max = len(v)
#            Max = max(Max, len(v))
#        return Max
        
#        a = sorted(pairs)
#        h = a[0]
#        ans = []
#        for block in a[1:]:
#            if h[1] < block[0]:
#                ans.append(h)
#                h = block
#            elif h[1] > block[1]:
#                h = block
#        return len(ans) + 1
        
        pairs = sorted(pairs)
        temp = pairs[0]
        ans = []
        for k in pairs[1:]:
            if temp[1] < k[0]:
                ans.append(temp)
                temp = k
            elif temp[1] > k[1]:
                temp = k
#            print(ans)
            print(k)
            print(temp)
        ans.append(temp) #此时的temp已经满足上面两种temp=k之一，只是上面最后一轮没有加
#        print(ans)
        return len(ans)
                
        
        
        
        
solu = Solution()
#pairs = [[1,2], [2,3], [3,4]]
#pairs = [[3,4], [2,3], [1,2]]
#pairs = [[7,9], [4,5], [7,9], [-7,-1], [0,10], [3,10], [3,6], [2,3]]
#pairs = [[-7, -1], [0, 10], [2, 3], [3, 10], [3, 6], [4, 5], [7, 9], [7, 9]]
#pairs = [[-7, -1], [0, 10], [2, 3], [3, 10], [3, 6], [-1, 5], [7, 9]]
pairs = [[-7, -1], [-1, 5], [0, 10], [2, 3], [3, 10], [3, 6], [3, 9]]
pairs = [[-7, -1], [-1, 5], [0, 10], [2, 3], [3, 10], [3, 6], [7, 9]]
print(solu.findLongestChain(pairs))