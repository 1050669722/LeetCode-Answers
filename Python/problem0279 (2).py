# class Solution:
#     def numSquares(self, n: int) -> int:
#         ans = []
#         for k in range(n, -1, -1):
#             while k != 0:
#                 if self.fun(k):
#                     ans.append(k)
#                     k = n-k
#                 else:
#                     break
#                 if sum(ans) + k == n:
#                     break
#         return ans

#     def fun(self, num):
#         return int(num**(1/2))**2 == num

# solu = Solution()
# n = 9
# print(solu.numSquares(n))


# class Solution:
#     def numSquares(self, n: int) -> int:
#         # dp = [0] * (n+1)
#         # dp[0] = 0
#         dp = [i for i in range(n+1)] #默认的拆法是都拆成全1相加
#         dp[0] = 0 #0默认认为不需要数相加
#         # print(dp)
#         for k in range(1, n+1):
#             p = 1
#             while k >= p**2:
#                 # print(dp[k], dp[k-p**2] + 1)
#                 dp[k] = min(dp[k], dp[k-p**2] + 1)
#                 p += 1
#         return dp[n]

# solu = Solution()
# n = 9
# print(solu.numSquares(n))


# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [i for i in range(n+1)] #默认的拆法是都拆成全1相加
#         dp[0] = 0 #0默认认为不需要数相加
#         for k in range(1, n+1):
#             #p是使得p**2不大于k的最大整数 但是12=9+1+1+1不如12=4+4+4
#             p = int(k ** (1/2))
#             dp[k] = min(dp[k], dp[k-p**2] + 1)
#         return dp[n]

# solu = Solution()
# n = 12#12#9
# print(solu.numSquares(n))


# 拉格朗日四数和定理
'''
定理内容：
每个正整数均可表示成不超过四个整数的平方之和

重要的推论：
数 n 如果只能表示成四个整数的平方和，不能表示成更少的数的平方之和，必定满足 4a(8b+7) 4^a(8b+7) 4a(8b+7)
如果 n%4==0，k=n/4，n 和 k 可由相同个数的整数表示
如何利用推论求一个正整数最少需要多少个数的平方和表示：
先判断这个数是否满足 4a(8b+7) 4^a(8b+7) 4a(8b+7)，如果满足，那么这个数就至少需要 4 个数的平方和表示。
如果不满足，再在上面除以 4 之后的结果上暴力尝试只需要 1 个数就能表示和只需要 2 个数就能表示的情况。
如果还不满足，那么就只需要 3 个数就能表示。
'''
class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        
        a = 0
        while a**2 <= n:
            b = int((n - a**2)**0.5)
            if a**2 + b**2 == n:
                return bool(a) + bool(b)
            a += 1
        
        return 3


