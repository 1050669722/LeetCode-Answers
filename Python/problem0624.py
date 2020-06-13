# from typing import List

# class Solution:
#     def maxDistance(self, arrays: List[List[int]]) -> int:
#         arrays.sort(key = lambda x: x[-1]-x[0])
#         print(arrays)
#         min_ = arrays[0][0]
#         max_ = arrays[0][-1]
#         for arr in arrays:
#             # min_ = min(min_, arr[0])
#             # max_ = max(max_, arr[-1])
#             mark1, mark2 = 0, 0
#             if arr[0] < min_:
#                 mark1 = 1
#             if arr[-1] > max_:
#                 mark2 = 1
#             if mark1 == 0 and mark2 == 0:
#                 pass
#             elif mark1 == 0 and mark2 != 0:
#                 max_ = arr[-1]
#             elif mark1 != 0 and mark2 == 0:
#                 min_ = arr[0]
#             else:
#                 tmp1 = min_ - arr[0]
#                 tmp2 = arr[-1] - max_
#                 if tmp1 > tmp2:
#                     min_ = arr[0]
#                 else:
#                     max_ = arr[-1]
#             # ans.append()
#             print(min_, max_)
#         return max_ - min_

# arrays = [[1,2,3],
#  [4,5],
#  [1,2,3]]
# arrays = [[1,4],[0,5]]
# arrays = [[1,5],[3,4]]
# # arrays = [[3,4],[1,5]]
# arrays = [[-1,1],[-3,1,4],[-2,-1,0,2]]
# solu = Solution()
# print(solu.maxDistance(arrays))


from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # arrays.sort(key = lambda x: x[-1] - x[0])
        # # min_ = min(arrays[0][0], arrays[1][0])
        # # max_ = max(arrays[0][-1], arrays[1][-1])
        # tmp1 = arrays[1][-1] - arrays[0][0]
        # tmp2 = arrays[0][-1] - arrays[1][0]
        # if tmp1 > tmp2:
        #     min_, max_ = arrays[0][0], arrays[1][-1]
        # else:
        #     min_, max_ = arrays[1][0], arrays[0][-1]
        
        # print(arrays)
        # print(tmp1, tmp2)
        # print(min_, max_)

        # for arr in arrays[2:]:
        #     if min_ <= arr[0] and arr[-1] <= max_:
        #         pass
        #     elif arr[0] < min_ and arr[-1] <= max_:
        #         min_ = arr[0]
        #     elif min_ <= arr[0] and max_ < arr[-1]:
        #         max_ = arr[-1]
        #     else:
        #         tmp1 = min_ - arr[0]
        #         tmp2 = arr[-1] - max_
        #         if tmp1 > tmp2:
        #             min_ = arr[0]
        #         else:
        #             max_ = arr[-1]
        # return max_ - min_

        min_, max_ = [], []
        for k, arr in enumerate(arrays):
            min_.append((arr[0], k))
            max_.append((arr[-1], k))
        min_.sort(key = lambda x: x[0])
        max_.sort(key = lambda x: x[0], reverse = True)
        # 其实到此时，就只有三种情况了
        for m in max_:
            if m[1] != min_[0][1]:
                tmp1 = m[0] - min_[0][0]
                break
        for m in min_:
            if m[1] != max_[0][1]:
                tmp2 = max_[0][0] - m[0]
                break
        return max(tmp1, tmp2)

arrays = [[1,4],[0,5]]
# arrays = [[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
solu = Solution()
print(solu.maxDistance(arrays))