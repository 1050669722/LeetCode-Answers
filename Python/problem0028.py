# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:34:39 2019

@author: Administrator
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        else:
            length = len(needle)
            for k in range(len(haystack)-length+1):
#                print(haystack[k:k+len(needle):1], needle)
                if haystack[k:k+length:1] == needle:
                    return k
            return -1
        
    def sunday_search(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        offset = {}
        n_l = len(needle)

        for i in range(n_l):
            offset[needle[i]] = n_l - i

        i, j, h_l = 0, 0, len(haystack)

        while i <= h_l - n_l:
            j = 0

            while haystack[i + j] == needle[j]:
                j += 1
                if j == n_l:
                    return i

            if i + n_l == h_l:
                return -1

            if haystack[i + n_l] in offset:
                i += offset[haystack[i + n_l]]
            else:
                i += n_l + 1

        return -1

    def kmp_search(self, haystack: str, needle: str) -> int:

        def get_next(pattern: str):
            j, k, l = 0, -1, len(pattern)

            p_next = [-1 for _ in range(l)]

            while j < l - 1:
                if k == -1 or pattern[j] == pattern[k]:
                    k += 1
                    j += 1
                    if pattern[j] != pattern[k]:
                        p_next[j] = k
                    else:
                        p_next[j] = p_next[k]
                else:
                    k = p_next[k]

            return p_next

        i, j, h_l, n_l = 0, 0, len(haystack), len(needle)
        p_next = get_next(needle)

        while i < h_l and j < n_l:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = p_next[j]

        if j == n_l:
            return i - j
        return -1
        
solu = Solution()
haystack, needle = "hello", 'll'
#haystack, needle = "a", 'a'
print(solu.strStr(haystack, needle))





