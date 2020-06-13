class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        mark = 0
        num_left = 0
        stack = []
        for letter in s:
            if letter == '(':
                mark += 1
                num_left += 1
            elif letter == ')':
                mark -= 1
            if mark < 0:
                mark += 1
            else:
                stack.append(letter) # 到这一步，stack中没有不合法的')'，不合法的右括号是指没有'('搭配的')'

        if mark == 0:
            return ''.join(stack)
        else:
            s = []
            tmp = num_left - mark
            count = 0
            for letter in stack:
                if letter == '(':
                    if count < tmp:
                        s.append(letter)
                    count += 1
                else:
                    s.append(letter)
            return ''.join(s)

s = "lee(t(c)o)de)"
# s = "a)b(c)d"
# s = "(a(b(c)d)"
# s = "())()((("
solu = Solution()
print(solu.minRemoveToMakeValid(s))