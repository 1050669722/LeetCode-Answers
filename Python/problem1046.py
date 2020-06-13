from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if x == y:
                continue
            else:
                stone = y - x
                stones.append(stone)
                stones.sort()
        return stones[0] if stones else 0
