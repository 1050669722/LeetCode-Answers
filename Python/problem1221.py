class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        count = 0
        for s0 in s:
            if s0 == 'L':
                count -= 1
            else:
                count += 1
            if count == 0:
                ans += 1
        return ans

