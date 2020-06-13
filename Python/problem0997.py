from typing import List

# class Solution:
#     def findJudge(self, N: int, trust: List[List[int]]) -> int:
#         # if N == 1 and not trust:
#         #     return 1
#         # if N > 1 and not trust:
#         #     return -1
#         # # max_ = trust[0][0]
#         # # candidates = set()
#         # # for t in trust:
#         # #     # max_ = max(max_, t[0], t[1])
#         # #     candidates.add(t[1])
#         # #     if t[0] in candidates:
#         # #         candidates.remove(t[0])
#         # # # print(candidates)
#         # # if not candidates:
#         # #     return -1
#         # candidates = set(range(1,N+1))
#         # d = {}
#         # for c in candidates:
#         #     d[c] = set()
#         # # print(d)
#         # for t in trust:
#         #     # if t[1] not in d:
#         #     #     continue
#         #     # else:
#         #     d[t[1]].add(t[0])
#         # print(d)
#         # res = []
#         # for k, v in d.items():
#         #     tmp = set(range(1, N+1))
#         #     tmp.remove(k)
#         #     if v == tmp:
#         #         res.append(k)
#         # if len(res) == 1:
#         #     return res[0]
#         # else:
#         #     return -1

#         if N == 1 and not trust:
#             return 1
#         if N > 1 and not trust:
#             return -1
#         # candidates = set(range(1,N+1))
#         d = {}
#         # for c in candidates:
#         #     d[c] = set()
#         # for t in trust:
#         #     d[t[1]].add(t[0])
#         for t in trust:
#             if t[1] not in d:
#                 d[t[1]] = set()
#                 d[t[1]].add(t[0])
#             else:
#                 d[t[1]].add(t[0])
#         res = set()
#         for k, v in d.items():
#             tmp = set(range(1, N+1))
#             tmp.remove(k)
#             if v == tmp:
#                 res.add(k)
#         for t in trust:
#             if t[0] in res:
#                 res.remove(t[0])
#         if len(res) == 1:
#             return list(res)[0]
#         else:
#             return -1

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        grid = [[0, 0] for _ in range(N)]
        for t in trust: #对trust的遍历方式与grid的更新方式有所不同
            grid[t[0]-1][0] += 1 #第t[0]-1个人信任别人(0)
            grid[t[1]-1][1] += 1 #第t[1]-1个人被别人信任(1)
        for k, g in enumerate(grid):
            if g[0] == 0 and g[1] == N-1:
                return k+1
        return -1

solu = Solution()
N = 2; trust = [[1,2]]
N = 3; trust = [[1,3],[2,3]]
N = 3; trust = [[1,3],[2,3],[3,1]]
N = 3; trust = [[1,2],[2,3]]
N = 4; trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
N = 2; trust = [[1,2],[2,1]]
N = 3; trust = [[1,3],[2,3],[3,1]]
print(solu.findJudge(N, trust))