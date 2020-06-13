# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:10:08 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:01:52 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

#class Solution(): #10:10 - 12:28
#    def romanToInt(self, s):
#        a = list(s)
#        b = []
##        temp = []
##        self.ans = []
##        special = ('IV','IX','XL','XC','CD','CM')
#        d = {'I':1,
#             'V':5,
#             'X':10,
#             'L':50,
#             'C':100,
#             'D':500,
#             'M':1000,#0-6
#             
#             'II':2,
#             'XX':20,
#             'CC':200,
#             'MM':2000,#7-10
#             
#             'III':3,
#             'XXX':30,
#             'CCC':300,
#             'MMM':3000,#11-14
#             
#             'IV':4,
#             'IX':9,
#             'XL':40,
#             'XC':90,
#             'CD':400,
#             'CM':900,}#15-20
#        special = list(d.keys())[15:21]
##        count = 0
#        while a != []: #a != None, bool(a), a
##            count += 1
##            print(a)
##            print(a!=[])
##            print(count)
##            print(len(a))
#            if len(a) >= 3:
#                b_temp = []
#                c1 = a.copy()
#                c2 = b.copy()
#                b_temp.append(''.join([a.pop(0),a.pop(0),a.pop(0)]))
#                b.append(b_temp[0])
##                b.append(a.pop(0))
##                b.append(a.pop(0))
##                print(''.join(b))
##                print(count)
##                print(b_temp[0])
#                if b_temp[0] not in list(d.keys())[11:14]:
##                    print(1)
#                    a = c1.copy()
#                    b = c2.copy()
##                    print(a)
##                    b.append(a.pop(0))
##                    temp.append(d[b])
##                print(count)
#            if len(a) >= 2:#try:
#                b_temp = []
#                c3 = a.copy()
#                c4 = b.copy()
#                b_temp.append(''.join([a.pop(0),a.pop(0)]))
#                b.append(b_temp[0])
##                b.append(a.pop(0))
##                b.append(a.pop(0))
##                print(''.join(b))
##                print(count)
##                print(b_temp[0])
#                if (b_temp[0] not in special) and (b_temp[0] not in list(d.keys())[7:10]):
##                    print(1)
#                    a = c3.copy()
#                    b = c4.copy()
##                    print(a)
#                    b.append(a.pop(0))
##                    temp.append(d[b])
##                print(count)
#            elif a:#except:
##                print(count)
###                print(2)
###                print(a)
#                b.append(a.pop(0))
##                temp.append(d[b])
##        return b
#        ans = 0
#        while b:
##            print(ans)
#            ans = ans * 10 + d[b.pop(0)]
#        return ans

#class Solution:
#    def romanToInt(self, s):
#        """
#        :type s: str
#        :rtype: int
#        """
#        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
#        ans=0        
#        for i in range(len(s)):            
#            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:              
#                ans-=a[s[i]]
#            else:
#                ans+=a[s[i]]
#        '''
#        从这个分支语句可以看出，对于问题的分解很重要，从哪个角度看待问题的分类
#        这里无非就是把这个问题当做 累加 或 累减
#        大于等于就做累加，小于就累减
#        但是它并不能判断罗马数字的正确与错误，当然也没有这个要求
#        '''
#        return ans


class Solution():
    def romanToInt(self, s):
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for k in range(len(s)-1):
            if a[s[k]] >= a[s[k+1]]:
                ans += a[s[k]]
            else:
                ans -= a[s[k]]
        ans += a[s[-1]]
        return ans
            
solu = Solution()
#s = "III"
#s = "IV"
#s = "IIIIV"
#s = "IX"
s = "LVIII"
#s = "MCMXCIV"
#solu.romanToInt(s)
print(solu.romanToInt(s))
#print(solu.romanToInt(s))
#print(type(solu.romanToInt(s)))

time2 = time.perf_counter()
print(time2-time1)
