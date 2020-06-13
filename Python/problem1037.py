from typing import List
import copy

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        tmp_points = copy.deepcopy(points)
        for k in range(len(tmp_points)):
            tmp_points[k] = tuple(tmp_points[k])
        if len(set(tmp_points)) != len(tmp_points):
            return False
        del tmp_points

        p1, p2, p3 = points[0], points[1], points[2]
        if p1[0] == p2[0]:
            k1 = 'inf'
        else:
            k1 = str(float( (p2[1]-p1[1])/(p2[0]-p1[0]) ))
        if p2[0] == p3[0]:
            k2 = 'inf'
        else:
            k2 = str(float( (p3[1]-p2[1])/(p3[0]-p2[0]) ))

        # if k1.isdigit(): print(1); k1 = float(k1)
        # if k2.isdigit(): print(2); k1 = float(k2)

        # if k1 != 'inf': print(1); k1 = float(k1)
        # if k2 != 'inf': print(2); k2 = float(k2)

        # print(k1, k2)

        return k1 != k2


solu = Solution()
points = [[1,1],[2,3],[3,2]]
# points = [[1,1],[2,2],[3,3]]
points = [[1,0],[0,0],[2,0]]
print(solu.isBoomerang(points))