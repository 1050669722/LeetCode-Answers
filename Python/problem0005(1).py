# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:36:25 2019

@author: Administrator
"""

# import time

# time1 = time.perf_counter()

# #class Solution(): #19:50 - 20:40
# #    def longestPalindrome(self, s):
# ##        st = {}
# ##        p = 0
# ##        for k in range(len(s)):
# ##            if s[k] in st.keys():
# ##                p = k
# ##            st[s[k]] = k
# #        
# #        length = len(s)
# #        if length == 0 or length == 1:
# #            return s
# ##        s_output = []
# #        else:
# #            for n in range(length,1,-1):
# #                a = []
# #                for p in range(0,length-n+1):
# #                    a.append(s[p:p+n])
# #                for m in range(len(a)):
# #                    if len(a[m]) % 2 == 0:
# #                        count = 0
# #                        for j in range(len(a[m]) // 2):
# #                            if a[m][0+j] != a[m][(len(a[m])-1)-j]:
# #                                count += 1
# #            #                    s_output.append(a[m])
# #                        if count == 0:
# #                            return a[m]    
# #                    else:
# #                        count = 0
# #                        for j in range((len(a[m])-1) // 2):
# ##                            print(0+j,(len(a[m])-1)-j)
# #                            if a[m][0+j] != a[m][(len(a[m])-1)-j]:
# ##                                print(a[m][0+j], a[m][(len(a[m])-1)-j])
# #                                count += 1
# #            #                    s_output.append(a[m])
# ##                        print(count)            
# #                        if count == 0:
# #                            return a[m]   
# #            return s[0]
# #    #                b = []
# #    #                c = {}
# #    #                for k in list(a[m]):
# #    #                    if k not in b:
# #    #                    	b.append(k)
# #    #                    	c[k] = 1
# #    #                    else:
# #    #                    	c[k] += 1
# #    #                count = 0
# #    #                for value in c.values():
# #    #                    if value != 1:
# #    #                        count += 1
# #    #                if count != 0:
# #    #                    continue
# #    #                else:
# #    #                    return a[m] #len(a[m]) 
# #
# #
# #class Solution(): #python3,滑动窗口（最好理解法）
# #    def longestPalindrome(self, s):
# #        if len(s) <= 1:
# #            return s
# #        max_s = s[0]
# #        for core in range(len(s) - 1):
# #            if s[core - 1] == s[core + 1] and core >= 1:
# #                r_range = min(core, len(s) - core - 1)
# #                for r1 in range(r_range + 1):
# #                    if s[core - r1] == s[core + r1]:
# #                        if 2 * r1 + 1 > len(max_s):
# #                            max_s = s[core - r1:core + r1 + 1]
# #                    else:
# #                        break
# #            if s[core] == s[core + 1]:
# #                r_range = min(core, len(s) - core - 2)
# #                for r2 in range(r_range + 1):
# #                    if s[core - r2] == s[core + r2 + 1]:
# #                        if 2 * r2 + 2 > len(max_s):
# #                            max_s = s[core - r2:core + r2 + 2]
# #                    else:
# #                        break
# #        return max_s

class Solution():
   def longestPalindrome(self, s):
       # Dynamic Programming  # 子序列是奇数个的情况 与 子序列是偶数列的情况
       if len(s) == 0:
           return ''
       if len(s) == 1:
           return s
       if len(s) == 2:
           if s[0] == s[1]:
               return s
           else:
               return s[0]
       ans = ''
       for k in range(1, len(s)-1):
           p = 0
           while 0<=k-p and k+p<=len(s)-1:
               if s[k-p] == s[k+p]:#and 0<=k-p and k+p<=len(s)-1:#
                   if len(ans)<=2*p+1:
                       ans = s[k-p:k+p+1]
               else:
                   break
               p += 1
       for k in range(1, len(s)-1):
           p = 0
           while 0<=k-p-1 and k+p<=len(s)-1:
               if s[k-p-1] == s[k+p]:#and 0<=k-p and k+p<=len(s)-1:#
                   if len(ans)<=2*p + 2:
                       ans = s[k-p-1:k+p+1]
               else:
                   break
               p += 1
       for k in range(1, len(s)-1):
           p = 0
           while 0<=k-p and k+p+1<=len(s)-1:
               if s[k-p] == s[k+p+1]:#and 0<=k-p and k+p<=len(s)-1:#
                   if len(ans)<=2*p + 2:
                       ans = s[k-p:k+p+2]
               else:
                   break
               p += 1
       return ans
                    

# class Solution():
#     def longestPalindrome(self, s):
#         # Dynamic Programming  # 子序列是奇数个的情况 与 子序列是偶数列的情况
        


# solu = Solution()
# s = 'cbbd'
# #s = 'cdbb'
# #s = 'babad'
# #s = 'bacsd'
# #s = 'ac'
# #s = 'abc'
# #s = ' '
# #s = ''
# #s = 'a'
# #s = 'ac'
# #s = 'bb'
# #s = 'abcda'
# #s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
# print(solu.longestPalindrome(s))

# time2 = time.perf_counter()
# print(time2-time1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for k in range(len(s)):
            if s[k] != s[0]:
                ans = s[0:k]
                break
            if k == len(s)-1:
                ans = s
        
        
        

















