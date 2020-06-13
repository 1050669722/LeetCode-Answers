class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # if not s:
        #     return 0

        # res = []
        # ans = 0
        # LeftStack, RightStack = [], []
        # for k in range(len(s)):
        #     if s[k] == '(':
        #         LeftStack.append(s[k])
        #     else:
        #         RightStack.append(s[k])
        #     if LeftStack and RightStack:
        #         ans += 2
        #         LeftStack.pop()
        #         RightStack.pop()
        #     if len(RightStack) > len(LeftStack):
        #         ans = 0


        # if not s:
        #     return 0
        
        # res = []
        # ans = 0
        # stack = [s[0]]
        # left, right = 0, 0
        # if s[0] == '(':
        #     left += 1
        # else:
        #     right += 1
        # for k in range(1, len(s)):
        #     if right > left:
        #         res.append(ans)
        #         ans = 0
        #         left = 0
        #         right = 0
        #     if stack and stack[-1] == '(' and s[k] == ')':
        #         stack.pop()
        #         left -= 1
        #         ans += 2
        #     else:
        #         stack.append(s[k])
        #         if s[k] == '(':
        #             left += 1
        #         else:
        #             right += 1
        # res.append(ans)
        # tmp1 = max(res)
        
        # s = [x for x in s]
        # for k in range(len(s)):
        #     if s[k] == '(':
        #         s[k] = ')'
        #     else:
        #         s[k] = '('
        # s = ''.join(s)
        
        # res = []
        # ans = 0
        # stack = [s[0]]
        # left, right = 0, 0
        # if s[0] == '(':
        #     left += 1
        # else:
        #     right += 1
        # for k in range(1, len(s)):
        #     if right > left:
        #         res.append(ans)
        #         ans = 0
        #         left = 0
        #         right = 0
        #     if stack and stack[-1] == ')' and s[k] == '(':
        #         stack.pop()
        #         right -= 1
        #         ans += 2
        #     else:
        #         stack.append(s[k])
        #         if s[k] == '(':
        #             left += 1
        #         else:
        #             right += 1
        # res.append(ans)
        # tmp2 = max(res)

        # print(tmp1, tmp2)
        # return min(tmp1, tmp2)

        def fun(s):
            if not s:
                return [0]
            res = []
            ans = 0
            stack = [s[0]]
            left, right = 0, 0
            if s[0] == '(':
                left += 1
            else:
                right += 1
            for k in range(1, len(s)):
                if right > left:
                    res.append(ans)
                    ans = 0
                    left = 0
                    right = 0
                if stack and stack[-1] == '(' and s[k] == ')':
                    stack.pop()
                    left -= 1
                    ans += 2
                else:
                    stack.append(s[k])
                    if s[k] == '(':
                        left += 1
                    else:
                        right += 1
            res.append(ans)
            return res#max(res)

        if not s:
            return 0

        TmpStack = [s[0]]
        inds = [0]
        for k in range(1, len(s)):
            if TmpStack and TmpStack[-1] == '(' and s[k] == ')':
                TmpStack.pop()
                inds.pop()
            else:
                TmpStack.append(s[k])
                inds.append(k)
        
        if not TmpStack:
            return len(s)
        elif TmpStack[-1] == ')':
            return max(fun(s))
        else:
            res = []
            res.append(max(fun(s[:inds[0]])))
            for i in range(1, len(inds)):
                res.append(max(fun(s[inds[i-1]+1:inds[i]])))
            res.append(max(fun(s[inds[-1]:])))
            return max(res)

# solu = Solution()
# s = "(()"
# # s = ")()())"
# # s = "())"
# # s = "()(()"
# # s = "()(())"
# # s = "()(()((("
# print(solu.longestValidParentheses(s))               


