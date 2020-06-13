class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = [-1]
        for k in range(len(s)):
            if s[k] == '(':
                stack.append(k)
            else:
                stack.pop()
                if stack:
                    maxans = max(maxans, k - stack[-1])
                else:
                    stack.append(k)
        return maxans

solu = Solution()
s = "(()"
# s = ")()())"
print(solu.longestValidParentheses(s))

