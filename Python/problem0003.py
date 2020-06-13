# # -*- coding: utf-8 -*-
# """
# Created on Sun May 12 17:25:45 2019

# @author: Administrator
# """

# import time

# time1 = time.perf_counter()

# #class Solution():
# #    def lengthOfLongestSubstring(self, s):
# #        length = len(s)
# ##        if length == 0:
# ##            return 0
# ##        elif length == 1:
# ##            return 1
# ##        else:
# #        for n in range(length,-1,-1):
# #            a = []
# #            for p in range(0,length-n+1):
# #                a.append(s[p:p+n])
# #            for m in range(len(a)):
# #                b = []
# #                c = {}
# #                for k in list(a[m]):
# #                    if k not in b:
# #                    	b.append(k)
# #                    	c[k] = 1
# #                    else:
# #                    	c[k] += 1
# ##                if 1 not in c.values():
# #                count = 0
# #                for value in c.values():
# #                    if value != 1:
# #                        count += 1
# #                if count != 0:
# #                    continue
# #                else:
# #                    return len(a[m]) #a[m]
                
# #class Solution:
# #    def lengthOfLongestSubstring(self, s):
# #        """
# #        :type s: str
# #        :rtype: int
# #        """
# #        st = {}
# #        i, ans = 0, 0
# #        for j in range(len(s)):
# #            if s[j] in st:
# #                i = max(st[s[j]], i) #上一个被重复字母的位置，以1开头
# #            ans = max(ans, (j + 1) - i) #这种相减是可行的，因为i是从1开始的
# #            st[s[j]] = (j + 1) #s[j]的位置更新，以1开头
# #        return ans

# class Solution():
#     def lengthOfLongestSubstring(self, s): #两个位置，当前字母的最新位置，被重复字母的最新位置
#         st = {}
#         i, ans = 0, 0
# #        d = {}
#         for j in range(len(s)): #一边计长度，一边更新最大长度值
#             if s[j] in st.keys():
# #                print(s[j])
# #                print([st[s[j]],i])
#                 i = max(st[s[j]], i)#st[s[j]]#
#             ans = max(ans, (j+1)-i)
# #            d['head'] = i
# #            d['tail'] = j+1
#             st[s[j]] = (j+1)
#         return ans
        
                    
# solu = Solution()
# s = 'abcabcbb'
# s = 'bbbbb'
# s = 'pwwkew'
# s = ''
# s = ' '
# s = 'c'
# s = 'au'
# s = "kwssiouw"#fydhihvgjuejmzbudeybgigseylmohjtgodovyxgubphcrbfxcjfkpxqpkfdsqz"
# print(solu.lengthOfLongestSubstring(s))

# time2 = time.perf_counter()
# print(time2-time1)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return s
        if len(set(s)) == 1:
            return 1
        p, q = 0, 0
        count = 0
        ans = 0
        while q <= len(s)-1:
            if self.fun(s[p:q+1]):
                print(1, p, q)
                ans = max(ans, q-p)
                q += 1
            else:
                print(2, p, q)
                ind = s[p:q+1].index(s[q]) + count
                count = len(s[p:q+1])
                p = ind + 1
                ans = max(ans, q-p)
                q += 1
        ans = max(ans, q-p)
        return ans

    def fun(self, s):
        if len(s) == len(set(s)):
            return True
        else:
            return False

solu = Solution()
s = "abcabcbb"
# s = "bbbbb"
# # s = "pwwkew"
# # s = ''
# # s = 's'
print(solu.lengthOfLongestSubstring(s))






