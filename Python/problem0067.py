# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:18:36 2019

@author: Administrator
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
#        ans = []
#        res = 0
#        p, q = len(a) - 1, len(b) - 1
#        while p>=0 and q>=0:
##            print(p,q)
#            res = res + int(a[p]) + int(b[q])
#            ans.append(str(res%2))
#            res //= 2
#            p -= 1
#            q -= 1
#        if res != 0:
#            ans.append(str(res))
##        print(p)
##        print(q)
#        if p >= 0:
##            a[len(a)-1:p-1:-1]
#            if (int(ans[-1])+int(a[p]))<2:
##                ans.pop()
##                print(ans[-1])
##                print(a[p])
#                ans.append(str(int(ans[-1])+int(a[p])))
#                ans.pop(-2)
#                while (p-1)>=0:
#                    p -= 1
#                    ans.append(a[p])
#            else:
##                ans.pop()
#                temp = ans[-1]
#                ans.append(str(0))
#                ans.pop(-2)
#                if (p-1)>=0:
#                    ans.append( str( (int(temp)+int(a[p]))//2+int(a[p-1]) ) )
##                    ans.pop(-2)
#                    if (p-2)>=0:
#                        p -= 2
#                        while p>=0:
#                            ans.append(a[p])
#                            p -= 1
#                else:
##                    print(str( (int(temp)+int(a[p])) ))
#                    ans.append( str( (int(temp)+int(a[p]))//2 ) )
#
#        if q >= 0:
##            a[len(a)-1:p-1:-1]
#            if (int(ans[-1])+int(b[q]))<2:
##                ans.pop()
##                print(ans[-1])
##                print(b[q])
#                ans.append(str(int(ans[-1])+int(b[q])))
#                ans.pop(-2)
#                while (q-1)>=0:
#                    q -= 1
#                    ans.append(b[q])
#            else:
##                ans.pop()
#                temp = ans[-1]
#                ans.append(str(0))
#                ans.pop(-2)
#                if (q-1)>=0:
#                    ans.append( str( (int(temp)+int(b[q]))//2+int(b[q-1]) ) )
##                    ans.pop(-2)
#                    if (q-2)>=0:
#                        q -= 2
#                        while q>=0:
#                            ans.append(b[q])
#                            q -= 1
#                else:
##                    print(str( (int(temp)+int(b[q])) ))
#                    ans.append( str( (int(temp)+int(b[q]))//2 ) )
#
#        if int(ans[-1]) > 1:
#            ans.append('0')
#            ans.pop(-2)
#            ans.append('1')
#        
#        ans.reverse()
#        ans = ''.join(ans)
#        return ans
        
        ans = []
        res = 0
        p, q = len(a) - 1, len(b) - 1
        while p>=0 and q>=0:
#            print(p,q)
            res = res + int(a[p]) + int(b[q])
            ans.append(str(res%2))
            res //= 2
            p -= 1
            q -= 1
        if res != 0:
            ans.append(str(res))
#        print(p)
#        print(q)
        if p >= 0:
#            a[len(a)-1:p-1:-1]
            if (int(ans[-1])+int(a[p]))<2:
#                ans.pop()
#                print(ans[-1])
#                print(a[p])
                ans.append(str(int(ans[-1])+int(a[p])))
                ans.pop(-2)
                while (p-1)>=0:
                    p -= 1
                    ans.append(a[p])
            else:
#                ans.pop()
                temp = ans[-1]
                ans.append(str(0))
                ans.pop(-2)
                if (p-1)>=0:
                    ans.append( str( (int(temp)+int(a[p]))//2+int(a[p-1]) ) )
#                    ans.pop(-2)
                    if (p-2)>=0:
                        p -= 2
                        while p>=0:
                            ans.append(a[p])
                            p -= 1
                else:
#                    print(str( (int(temp)+int(a[p])) ))
                    ans.append( str( (int(temp)+int(a[p]))//2 ) )

        if q >= 0:
#            a[len(a)-1:p-1:-1]
            if (int(ans[-1])+int(b[q]))<2:
#                ans.pop()
#                print(ans[-1])
#                print(b[q])
                ans.append(str(int(ans[-1])+int(b[q])))
                ans.pop(-2)
                while (q-1)>=0:
                    q -= 1
                    ans.append(b[q])
            else:
#                ans.pop()
                temp = ans[-1]
                ans.append(str(0))
                ans.pop(-2)
                if (q-1)>=0:
                    ans.append( str( (int(temp)+int(b[q]))//2+int(b[q-1]) ) )
#                    ans.pop(-2)
                    if (q-2)>=0:
                        q -= 2
                        while q>=0:
                            ans.append(b[q])
                            q -= 1
                else:
#                    print(str( (int(temp)+int(b[q])) ))
                    ans.append( str( (int(temp)+int(b[q]))//2 ) )

        if int(ans[-1]) > 1:
            ans.append('0')
            ans.pop(-2)
            ans.append('1')
        
        ans.reverse()
        ans = ''.join(ans)
        return ans
        
solu = Solution()
#a, b = "11", "1"
a, b = "1010", "1011"
a, b = "1", "11"
a, b = "1", "111"
a, b = "111", "1"
print(solu.addBinary(a, b))