# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:32:55 2019

@author: Administrator
"""

# import time

# time1 = time.perf_counter()

# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
# #        if J == '' or S == '':
# #            return 0
# #        else:
# #            count = 0
# #            for p in J:
# #                for q in S:
# #                    if p == q:
# #                        count += 1
# #        return count
#         if J == '' or S == '':
#             return 0
#         else:
#             d = {}
#             count = 0
#             for p in S:
#                 try:
#                     d[p] += 1
#                 except:
#                     d[p] = 1
#             for q in J:
#                 try:
#                     count += d[q]
#                 except:
#                     pass
#         return count


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if J == '' or S == '':
            return 0
        
        J = set(J)
        
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count




solu = Solution()
#J, S = 'aA', 'aAAbbbb'
#J, S = 'z', 'ZZ'
J = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW'
S = 'ARQNIURVQURwogqrXYZhgorivpreoirqinroeivpreoirqinroeivpreoirqinroeivpreoirqinroeivpreoirqinroeivpreoirqinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoioirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqiinroeivpreoirqinroeivpreoirqinroeivpreoirqinroeivpreoirqinroeivpreoirqinroetbetbqetbeQRGEBQEBTHQUEQVFQNPQVFQNPQVFQNPQVFQNPQVFQNPQVF'
print(solu.numJewelsInStones(J, S))

time2 = time.perf_counter()
print(time2 - time1)

