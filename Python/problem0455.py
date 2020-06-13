class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        '''
        这一题很像华为面试的第一题：优势洗牌
        不过，那一题是要求把s重新排序以满足g
        '''
#         count = 0
#         for g0 in g:
#             s.append(g0)
#             s.sort()#g = self.CountSort(g)#
#             ind = s.index(g0)
#             if ind != len(s)-1:
#                 count += 1
#                 del s[ind]
#                 del s[ind]
#             else:
#                 s.pop()
#         return count

# # solu = Solution()
# # g, s = [1,2,3], [1,1]
# # g, s = [1,2], [1,2,3]
# # print(solu.findContentChildren(g, s))


#         count = 0
#         for g0 in g:
#             s.append(g0)
#             s.sort()#g = self.CountSort(g)#
#             ind = s.index(g0)
#             if ind != len(s)-1:
#                 count += 1
#                 del s[ind]
#                 del s[ind]
#             else:
#                 s.pop()
#         return count

#     def CountSort(self, nums):
#         MIN = min(nums)
#         for k in range(len(nums)):
#             nums[k] -= MIN
#         tmp = [0] * (max(nums)+1)
#         for num in nums:
#             tmp[num] += 1
#         ans = []
#         for k in range(len(tmp)):
#             for _ in range(tmp[k]):
#                 ans.append(k)
#         for k in range(len(ans)):
#             ans[k] += MIN
#         return ans

# # solu = Solution()
# # g, s = [1,2,3], [1,1]
# # g, s = [1,2], [1,2,3]
# # print(solu.findContentChildren(g, s))


        g.sort(), s.sort()
        p, q, ans = 0, 0, 0
        while p<len(s) and q<len(g):
            if s[p] >= g[q]:
                ans += 1
                p += 1
                q += 1
            else:
                p += 1
        return ans


solu = Solution()
g, s = [1,2,3], [1,1]
g, s = [1,2], [1,2,3]
print(solu.findContentChildren(g, s))