class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        mark = 0
        stack = []
        for s in S:
            if s == '(':
                if mark != 0:
                    stack.append(s)
                mark += 1
            if s == ')':
                mark -= 1
                if mark != 0:
                    stack.append(s)
        return ''.join(stack)

solu = Solution()
# S = "(()())(())"
# S = "(()())(())(()(()))"
# S = "()()"
S = '(()())(())))))))'
print(solu.removeOuterParentheses(S))




