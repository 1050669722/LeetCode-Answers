from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # marks = [0] * (len(coordinates)-1)
        slopes = []
        for k in range(1, len(coordinates)):
            x0, y0 = coordinates[k-1][0], coordinates[k-1][1]
            x1, y1 = coordinates[k][0], coordinates[k][1]
            if x1 == x0:
                # marks[k-1] == 1
                slopes.append('inf')
            else:
                slopes.append((y1-y0)/(x1-x0))
            if len(slopes) > 1:
                if slopes[-1] != slopes[-2]:
                    return False
        return True