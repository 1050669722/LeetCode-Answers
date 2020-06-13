class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        '''
        这是要找子数组的，
        不能排序
        '''
#         sumlist = [0] * len(nums)
#         sumlist[0] = nums[0]
#         for p in range(1, len(nums)):
#             sumlist[p] = sumlist[p-1] + nums[p]
#         count = 0
#         for start in range(len(nums)):
#             for end in range(start, len(nums)):
#                 tmp = sumlist[end] - sumlist[start] + nums[start]
#                 # print('***', tmp, '***')
#                 if tmp == k:
#                     count += 1
#         return count

# # solu = Solution()
# # nums, k = [1,1,1], 2
# # nums, k = [1,2,3], 3
# # nums, k = [-1, -1, 1], 0
# # print(solu.subarraySum(nums, k))


        d = {0:1} #默认和0情况出现了一次
        Sum = 0
        count = 0
        for p in range(len(nums)):
            Sum += nums[p]
            # if d.__contains__(Sum-k): #k=0是一种特殊情况
            count += d.get(Sum-k, 0)
            # d.setdefault(Sum, d.get(Sum, 0)+1)
            d.setdefault(Sum, 0)
            d[Sum] += 1
        print(d)
        return count

solu = Solution()
nums, k = [1,1,1], 2
# nums, k = [1,2,3], 3
# nums, k = [-1, -1, 1], 0
print(solu.subarraySum(nums, k))

