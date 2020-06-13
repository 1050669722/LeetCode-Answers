class Solution:
    def findMinDifference(self, timePoints: list) -> int:
        for k in range(len(timePoints)):
            tmp = timePoints[k]
            tmp = tmp.split(':')
            tmp = [int(x) for x in tmp]
            tmp = tmp[0]*60 + tmp[1]
            timePoints[k] = tmp
        timePoints.sort()
        # print(timePoints)
        ans = float('inf')
        for k in range(1, len(timePoints)):
            tmp = timePoints[k]-timePoints[k-1]
            tmp = min(tmp, 1440-tmp)
            ans = min(ans, tmp)
        tmp = timePoints[-1]-timePoints[0]
        tmp = min(tmp, 1440-tmp)
        ans = min(ans, tmp)        
        return ans

# solu = Solution()
# timePoints = ["05:31","22:08","00:35"]
# print(solu.findMinDifference(timePoints))
