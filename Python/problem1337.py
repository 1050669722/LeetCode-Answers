from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for num, line in enumerate(mat):
            arr.append( (num, sum(line)) )
        arr.sort(key = lambda x: x[1])
        res = []
        for num in range(k):
            res.append(arr[num][0])
        return res

solu = Solution()
mat = [[1,1,0,0,0],
       [1,1,1,1,0],
       [1,0,0,0,0],
       [1,1,0,0,0],
       [1,1,1,1,1]]
k = 3
ans = solu.kWeakestRows(mat, k)
print(ans)