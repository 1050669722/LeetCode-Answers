from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # costs.sort(reverse = True, key = lambda x: abs(x[0]-x[1]))
        
        # A, B = [], []
        # d = {}
        # for cost in costs:
        #     if cost[0] < cost[1]:
        #         A.append(cost)
        #     else:
        #         B.append(cost)
        #     if str(cost) in d:
        #         d[str(cost)] += 1
        #     else:
        #         d[str(cost)] = 1
        # A.sort(reverse = True, key = lambda x: x[0])
        # B.sort(reverse = True, key = lambda x: x[1])

        # ans = 0
        # for cost in costs:
        #     if cost[0] < cost[1]:
        #         ans += cost[0]
        #         d[str(cost)] -= 1
        #         mark = 0
        #         while B:
        #             tmp = B.pop()
        #             if d[str(tmp)] > 0:
        #                 ans += tmp[1]
        #                 d[str(tmp)] -= 1
        #                 mark = 1
        #                 break
        #         if mark == 0:
        #             while A:
        #                 tmp = A.pop()
        #                 if d[str(tmp)] > 0:
        #                     ans += tmp[1]
        #                     d[str(tmp)] -= 1
        #                     mark = 1
        #                     break
        #         if mark == 0:
        #             return ans
        #     else:
        #         ans += cost[1]
        #         d[str(cost)] -= 1
        #         mark = 0
        #         while A:
        #             tmp = A.pop()
        #             if d[str(tmp)] > 0:
        #                 ans += tmp[0]
        #                 d[str(tmp)] -= 1
        #                 mark = 1
        #                 break
        #         if mark == 0:
        #             while B:
        #                 tmp = B.pop()
        #                 if d[str(tmp)] > 0:
        #                     ans += tmp[0]
        #                     d[str(tmp)] -= 1
        #                     mark = 1
        #                     break
        #         if mark == 0:
        #             return ans

        costs.sort(key = lambda x: x[0] - x[1]) #x[0] - x[1]可以理解为去A的有利程度
        ans = 0
        n = len(costs) // 2
        # for k in range(0, n):
        #     ans += costs[k][0] + costs[k+n][1]
        # return ans
        for k in range(0, n):
            ans += costs[k][0]
        for k in range(n, 2*n):
            ans += costs[k][1]
        return ans

solu = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
print(solu.twoCitySchedCost(costs))