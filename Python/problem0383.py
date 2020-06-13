# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:06:36 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#        return set(magazine)&set(ransomNote) == set(ransomNote)
        n = list(magazine)
        for k in ransomNote:
            try:
                n.remove(k)
            except:
                return False
        return True
        
#        a, b = {}, {}
#        for k in ransomNote:
#            try:
#                a[k] += 1
#            except:
#                a[k] = 1
#        for k in magazine:
#            try:
#                b[k] += 1
#            except:
#                b[k] = 1
#        count = 0
#        for key in a.keys():
#            try:
#                if a[key] <= b[key]:
#                    count += 1
#            except:
#                return False
#        if count == len(a.keys()):
#            return True
#        else:
#            return False

solu = Solution()
#ransomNote, magazine = "a", "b"
#ransomNote, magazine = "aa", "ab"
ransomNote, magazine = "aa", "aab"
ransomNote, magazine = "aaqEGQETHWRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHWsrtrhghrnaaqEGQETHRYNWRTHHWsrtrhghrnaaqEGQETHWRYNWRTHHWsrtrhghrnaaqEGQETHWRYNWRTHHWsrtrhghrnaaqEGQETHWRYNWRTHHWsrtrhghrnaaqEGQETHWRYNWRTHHWsrtrhghrn", "aabgwesthwryraqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNaqettRWRYSRNRYWRYMNWNWWRYMSGghwrst"
print(solu.canConstruct(ransomNote, magazine))

time2 = time.perf_counter()
print(time2 - time1)