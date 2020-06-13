# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:55:45 2019

@author: ASUS
"""

from collections import defaultdict

class Solution:
    def highFive(self, items: list) -> list:
        ans = []
        d = defaultdict()#{}#
        for k in range(len(items)):
            try:
                d[items[k][0]].append(items[k][1])
            except:
                d[items[k][0]] = []
                d[items[k][0]].append(items[k][1])
#        d = defaultdict(list)
#        for k in range(len(items)):
#            d[items[k][0]].append(items[k][1])
        for key, value in d.items():
#            value.sort(reverse=True) #列表的当场改变，就算列表作为字典的值，也是有效的
            value.sort()
            value = value[::-1]
            ans.append([])
            ans[-1].append(key)
            mean = sum(value[:5])//5
            ans[-1].append(mean)
        return ans
            
solu = Solution()
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(solu.highFive(items))
        