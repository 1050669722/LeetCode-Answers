from typing import List

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        # if not (A and B):
        #     return A
        # d = {}
        # for k in range(len(B)):
        #     d[B[k]] = [k]
        # A.sort()
        # B.sort()
        # for k in range(len(B)):
        #     d[B[k]].append(k)
        # ans = []
        # tmp = []
        # p, q = 0, 0
        # while p < len(A) and q < len(B):
        #     if A[p] > B[q]:
        #         ans.append(A[p])
        #         p += 1
        #         q += 1
        #     else:
        #         tmp.append(A[p])
        #         p += 1
        # ans = ans + tmp
        # s = set()
        # for value in d.values():
        #     tmp = value
        #     s.add(tmp[0])
        #     if tmp[1] not in s:
        #         ans[tmp[0]], ans[tmp[1]] = ans[tmp[1]], ans[tmp[0]]
        # return ans
        
        # if not (A and B):
        #     return A
        # k = 0
        # sA, sB = sorted(A), sorted(B)
        # d, D = {}, {}
        # for a in sA:
        #     if a > sB[k]:
        #         d[sB[k]] = a
        #         k += 1
        #     else:
        #         D[sB[k]] = a
        # print(d)
        # print(D)
        # ans = []
        # for b in B:
        #     try:
        #         ans.append(d[b])
        #     except:
        #         ans.append(D[b])
        # return ans

        if not (A and B):
            return A
        sortedA, sortedB = sorted(A), sorted(B)
        d = {b:[] for b in B}
        tmp = []
        k = 0
        for a in sortedA:
            if a > sortedB[k]:
                d[sortedB[k]].append(a)
                k += 1
            else:
                tmp.append(a)
        return [d[b].pop() if d[b] else tmp.pop() for b in B]


solu = Solution()
A, B = [2,7,11,15], [1,10,4,11]
# A, B = [12,24,8,32], [13,25,32,11]
print(solu.advantageCount(A, B))

