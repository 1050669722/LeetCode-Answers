class Solution:
    def trapRainWater(self, heightMap: list) -> int:
        import numpy as np
        ans = 0

        for _ in range(20000):
            rec = [ [0] * len(heightMap[0]) for _ in range(len(heightMap)) ]
            for p in range(1, len(heightMap)-1):
                for q in range(1, len(heightMap[0])-1):
                    tmp = min(heightMap[p-1][q], heightMap[p+1][q], heightMap[p][q-1], heightMap[p][q+1])
                    ans += max(tmp - heightMap[p][q], 0)
                    rec[p][q] = max(tmp - heightMap[p][q], 0)
            heightMap = np.array(heightMap)
            rec = np.array(rec)
            heightMap += rec
            heightMap.tolist()
            # print(ans)
            # print(heightMap)
        
        return ans

solu = Solution()
heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
print(solu.trapRainWater(heightMap))



