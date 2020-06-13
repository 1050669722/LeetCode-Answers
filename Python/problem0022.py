# class Solution(object):
#     def generateParenthesis(self, N):
#         ans = []
#         def backtrack(S = '', left = 0, right = 0):
#             if len(S) == 2 * N:
#                 ans.append(S)
#                 # print(ans)
#                 return
#             # print(left, right)
#             # 下面这两个if有可能都被运行
#             # 左括号不到一半数 则添加 左括号
#             # 右括号不满左括号 则添加 右括号
#             if left < N:
#                 backtrack(S+'(', left+1, right)
#             if right < left:
#                 backtrack(S+')', left, right+1)

#         backtrack()
#         return ans

# # solu = Solution()
# # # n = 1
# # n = 2
# # # n = 3
# # solu.generateParenthesis(n)
# # # print(solu.generateParenthesis(n))


class Solution:
    def generateParenthesis(self, n: int) -> list:
        ans = []
        
        def backtrack(S, left, right):
            if len(S) == 2*n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        
        backtrack('', 0, 0)
        return ans

# solu = Solution()
# n = 1
# # n = 2
# # n = 3
# solu.generateParenthesis(n)
# print(solu.generateParenthesis(n))