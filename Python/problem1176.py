# from typing import List

# class Solution:
#     def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
#         ans = 0
#         for p in range(0, len(calories)-k+1):
#             tmp = sum(calories[p:(p+k)])
#             if tmp < lower:
#                 ans -= 1
#             elif tmp > upper:
#                 ans += 1
#         return ans


from typing import List

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = 0
        tmp = sum(calories[:k])

        # 滑动窗口 的 滑动过程
        for p in range(1, len(calories)-k+1):
            if tmp < lower:
                ans -= 1
            elif tmp > upper:
                ans += 1
            tmp -= calories[p-1]
            tmp += calories[p-1+k]
        
        if tmp < lower:
            ans -= 1
        elif tmp > upper:
            ans += 1
        return ans

solu = Solution()
calories, k, lower, upper = [1,2,3,4,5], 1, 3, 3
# calories, k, lower, upper = [6,5,0,0], 2, 1, 5
# calories, k, lower, upper = [3,2], 2, 0, 1
print(solu.dietPlanPerformance(calories, k, lower, upper))