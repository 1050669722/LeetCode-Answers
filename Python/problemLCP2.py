# class Solution:
#     def fraction(self, cont: list) -> list:
#         if not cont:
#             return None
#         if len(cont) == 1:
#             return [1, cont[0]]
#         a = cont[1:]
#         tmp = a.pop()
#         if tmp == 0:
#             return None
#         res = tmp
#         if len(a)%2 == 0:
#             while a:
#                 res = 1/res
#                 tmp = a.pop()
#                 res += tmp
#             ans = res*cont[0] + 1
#             b = self.gcd(ans, res)
#             return [int(ans//b), int(res//b)]
#         else:
#             while a:
#                 res = 1/res
#                 tmp = a.pop()
#                 res += tmp
#             ans = res*cont[0] + 1
#             ans, res = res, ans
#             ans = 1/ans
#             b = self.gcd(ans, res)
#             return [int(ans//b), int(res//b)]
    
#     def gcd(self, a, b):
#         if b == 0:
#             return a
#         else:
#             return self.gcd(b, a%b)

# # solu = Solution()
# # cont = [3, 2, 0, 2]
# # cont = [0, 0, 3]
# # print(solu.fraction(cont))


# class Solution:
#     def fraction(self, cont: List[int]) -> List[int]:
#         res=[cont[-1],1]
#         length=len(cont)
#         for i in range(length-1,0,-1):
#             temp=res[1]
#             res[1]=res[0]
#             res[0]=cont[i-1]*res[1]+temp
#         return res

# # 作者：george-26
# # 链接：https://leetcode-cn.com/problems/deep-dark-fraction/solution/python3-xian-xing-shi-jian-by-george-26/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def fraction(self, cont: list) -> list:
        ans = [cont[-1], 1]
        for k in range(len(cont)-1, 0, -1):
            tmp = ans[1]
            ans[1] = ans[0]
            ans[0] = cont[k-1]*ans[1] + tmp
        return ans

# solu = Solution()
# cont = [3, 2, 0, 2]
# cont = [0, 0, 3]
# print(solu.fraction(cont))


