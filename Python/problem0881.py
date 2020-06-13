from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        p, q = 0, len(people)-1
        ans = 0
        # print(ans)
        while p <= q:
            ans += 1
            if people[p] + people[q] > limit:
                p += 1
            else:
                p += 1
                q -= 1
        return ans

people = [1,2]; limit = 3
people = [3,2,2,1]; limit = 3
people = [3,5,3,4]; limit = 5
solu = Solution()
print(solu.numRescueBoats(people, limit))