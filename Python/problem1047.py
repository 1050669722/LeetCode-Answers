class Solution:
    def removeDuplicates(self, S: str) -> str:
        '''
        有点像消消乐
        '''
        stack = [S[0]]
        p, q = 1, 0
        while p < len(S):
            # p += 1
            if q < 0:
                stack.append(S[p])
                q += 1
            else:
                # print(p, q, stack)
                if S[p] == stack[q]:
                    stack.pop()
                    q -= 1
                else:
                    stack.append(S[p])
                    q += 1
            p += 1
        return ''.join(stack)

'''
accaca
'''

# solu = Solution()
# S = 'accaca'
# print(solu.removeDuplicates(S))

# class Solution:
#     def removeDuplicates(self, S: str) -> str:
#         output = []
#         for ch in S:
#             if output and ch == output[-1]: 
#                 output.pop()
#             else: 
#                 output.append(ch)
#         return ''.join(output)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/solution/shan-chu-zi-fu-chuan-zhong-de-suo-you-xiang-lin-zh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。