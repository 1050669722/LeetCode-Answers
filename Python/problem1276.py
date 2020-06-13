from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 == 1:
            return []
        
        # y = tomatoSlices - cheeseSlices - 3 * (cheeseSlices - y)
        # y = tomatoSlices - cheeseSlices - 3 * cheeseSlices + 3 * y
        # -2 * y = tomatoSlices - cheeseSlices - 3 * cheeseSlices
        # -2 * y = tomatoSlices - 4 * cheeseSlices
        # 2 * y = - tomatoSlices + 4 * cheeseSlices
        y = 2 * cheeseSlices - (1/2) * tomatoSlices
        
        if y >= 0 and y == int(y) and cheeseSlices-y >= 0:
            return [int(cheeseSlices-y), int(y)]
        else:
            return []