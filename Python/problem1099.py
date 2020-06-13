from typing import List

# class Solution:
#     def twoSumLessThanK(self, A: List[int], K: int) -> int:
#         A.sort(reverse = True)
#         mark = 0
#         ans = 0
#         print(A)
#         for k in range(len(A)-1):
#             if A[k] + A[k+1] <= K:
#                 ans = max(ans, A[k] + A[k+1])
#                 mark = 1
#         if mark == 1:
#             return ans
#         else:
#             return -1


# from typing import List

# class Solution:
#     def twoSumLessThanK(self, A: List[int], K: int) -> int:
#         A.sort()
#         p, q = 0, len(A)-1
#         ans = []
#         while p < q:
#             tmp = A[p] + A[q]
#             # if  tmp == K:
#             #     return tmp
#             # elif tmp > K:
#             #     q -= 1
#             # else:
#             #     ans.append(tmp)
#             #     p += 1
#             if tmp > K:
#                 q -= 1
#             elif tmp < K:
#                 ans.append(tmp)
#                 p += 1
#         if ans:
#             return max(ans)
#         else:
#             return -1


from typing import List
# import sys

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        # if not A:
        #     return 0
        # if len(A) < 2:
        #     return A[0] if A[0] < K else -1
        if len(A) < 2:
            return -1
        
        A.sort()
        p, q = 0, len(A)-1
        # ans = int('inf')
        # ans = int('-inf')
        # ans = sys.maxsize
        # ans = sys.minsize
        # ans = A[0] + A[1]
        ans = -1
        while p < q:
            tmp = A[p] + A[q]
            # print(tmp)
            if tmp >= K:
                q -= 1
            elif tmp < K:
                ans = max(ans, tmp)
                p += 1
        # if ans < K:
        #     return ans
        # else:
        #     return -1
        return ans

solu = Solution()
A, K = [34,23,1,24,75,33,54,8], 60
A, K = [10, 20, 30], 15
A, K = [100], 200
A, K = [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944], 200
print(solu.twoSumLessThanK(A, K))