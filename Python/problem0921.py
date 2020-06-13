class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        mark = 0
        ans = 0
        for s in S:
            if s == '(':
                mark += 1
            if s == ')':
                mark -= 1
            if mark < 0:
                mark += 1
                ans += 1
        ans += mark
        return ans

S = "())"
# S = "((("
# S = "()"
# S = "()))(("
solu = Solution()
print(solu.minAddToMakeValid(S))