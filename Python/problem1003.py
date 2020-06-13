class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for s in iter(S):
            if len(stack) >= 2 and ''.join(stack[-2:]) + s == 'abc':
                    stack.pop()
                    stack.pop()
            else:
                stack.append(s)
        return not stack

S = "abc"
# S = "aabcbc"
S = "abcabcababcc"
S = "abccba"
S = "cababc"
solu = Solution()
print(solu.isValid(S))