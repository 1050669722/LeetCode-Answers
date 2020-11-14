# from typing import List

# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         d = {}
#         for a in arr2:
#             d[a] = 0
#         tmp = []
#         for a in arr1:
#             if a in d:
#                 d[a] += 1
#             else:
#                 tmp.append(a)
#         ans = []
#         for k, v in d.items():
#             for _ in range(v):
#                 ans.append(k)
#         tmp.sort()
#         ans.extend(tmp)
#         return ans

# arr1 = [2,3,1,3,2,4,6,7,9,2,19]; arr2 = [2,1,4,3,9,6]
# solu = Solution()
# print(solu.relativeSortArray(arr1, arr2))


from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if arr1 == [] or arr2 == []:
            return arr1
        
        counter = Counter(arr1)
        ans = []
        for a in arr2:
            for _ in range(counter[a]):
                ans.append(a)
        tmp = list(set(arr1) - set(arr2))
        res = []
        for t in tmp:
            for _ in range(counter[t]):
                res.append(t)
        ans += sorted(res)
        return ans
    
