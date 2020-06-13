# class Solution:
#     def findNumberOfLIS(self, nums: list) -> int:
#         if not nums:
#             return 0
        
#         if len(nums) == 1:
#             return 1

#         for k in range(1, len(nums)):
#             if nums[k] >= nums[k-1]:
#                 ind = k-1
#                 break
#         try:
#             nums = nums[ind:]
#         except:
#             return 0

#         d_count = {}
#         lengths  = [1] * len(nums) #初始化dp数组
#         for i in range(len(lengths )):
#             count = 0
#             for j in range(i-1, -1, -1): #j: i-1 -> 0
#                 if nums[i] > nums[j]:
#                     lengths [i] = lengths [j] + 1 #累计可以成为递增子序列的搭配
#                     for k in range(j-1, -1, -1):
#                         if nums[i] <= nums[k]:
#                             count += 1#int(bool(lengths [k]-1)) #统计不能成为递增子序列的搭配
#                     break
#             d_count[nums[i]] = count
#         print(lengths )
#         d = {}
#         MAX = max(lengths )
#         lengths .reverse()
#         ind = lengths .index(MAX)
#         lengths .reverse()
#         ind = len(lengths )-1 - ind #dp中最大数的最后一个索引
#         for n in lengths [:ind+1]: #在dp数组中，不超过这个索引，统计所有元素出现的频数
#             try:
#                 d[n] += 1
#             except:
#                 d[n] = 1
#         print(d)
#         ans = 1
#         for value in d.values():
#             ans *= value
#         for value in d_count.values():
#             ans -= value
#         print(d_count)
#         return ans

# solu = Solution()
# # nums = [1,3,5,4,7]
# # nums = [2,2,2,2,2]
# # nums = [1,3,5,4,8,7,6,2,0]
# # nums = [10,9,8,9,10,11,12]
# # nums = [1]
# # nums = []
# # nums = [1,2,4,3,5,4,7,2]
# # nums = [100,90,80,70,60,50,60,70,80,90,100]
# nums = [1,2,10,9,8,9,10,11,12]
# print(solu.findNumberOfLIS(nums))


# # class Solution:
# #     def findNumberOfLIS(self, nums: list) -> int:
# #         if not nums:
# #             return 0

# #         lengths  = [1] * len(nums) #初始化dp数组
# #         for i in range(len(lengths )):
# #             for j in range(i-1, -1, -1): #j: i-1 -> 0
# #                 if nums[i] > nums[j]:
# #                     lengths [i] = lengths [j] + 1 #累计 可以成为递增子序列的搭配
# #                 elif nums[i] == nums[j] and lengths [j] != 1: #如果前面已经有相同的数，并且已经开始累计
# #                     lengths [i] = lengths [j]
# #         print(lengths )
# #         d = {}
# #         MAX = max(lengths )
# #         lengths .reverse()
# #         ind = lengths .index(MAX)
# #         lengths .reverse()
# #         ind = len(lengths )-1 - ind #dp中最大数的最后一个索引
# #         for n in lengths [:ind+1]: #在dp数组中，不超过这个索引，统计所有元素出现的频数
# #             try:
# #                 d[n] += 1
# #             except:
# #                 d[n] = 1
# #         print(d)
# #         ans = 1
# #         for value in d.values():
# #             ans *= value
# #         # for value in d_count.values():
# #         #     ans -= value
# #         # print(d_count)
# #         return ans

# # solu = Solution()
# # # nums = [1,3,5,4,7]
# # # nums = [2,2,2,2,2]
# # # nums = [1,3,5,4,8,7,6,2,0]
# # # nums = [10,9,8,9,10,11,12]
# # # nums = [1]
# # # nums = []
# # # nums = [1,2,4,3,5,4,7,2]
# # # nums = [100,90,80,70,60,50,60,70,80,90,100]
# # nums = [1,2,10,9,8,9,10,11,12]
# # print(solu.findNumberOfLIS(nums))


class Solution(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        lengths  = [0] * N #lengths [i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j in range(len(nums)):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths [i] >= lengths [j]:
                        lengths [j] = 1 + lengths [i]
                        counts[j] = counts[i]
                    elif lengths [i] + 1 == lengths [j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths [i] == longest)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/zui-chang-di-zeng-zi-xu-lie-de-ge-shu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。