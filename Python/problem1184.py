from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        # print(start, destination)
        tmp = destination - len(distance)
        # print(tmp)
        ans1 = sum(distance[start:destination])
        # print(distance[start:destination])
        # ans2 = sum(distance[start-1:tmp-1:-1])
        ans2 = sum(distance[0:start]) + sum(distance[destination:])
        # print(distance[start-1:tmp-1:-1])
        return min(ans1, ans2)

# solu = Solution()
# distance, start, destination = [1,2,3,4], 0, 1
# distance, start, destination = [1,2,3,4], 0, 2
# distance, start, destination = [1,2,3,4], 0, 3
# distance, start, destination = [7,10,1,12,11,14,5,0], 7, 2
# print(solu.distanceBetweenBusStops(distance, start, destination))