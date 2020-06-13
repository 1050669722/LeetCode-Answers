class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # mark = 0
        # count = 0
        # # m = 0
        # for s in S:
        #     if s == '(':
        #         mark += 1
        #     else:
        #         mark -= 1
        #         # if mark != 0 and m != 0:
        #         count += 1 * 2**mark
        #         # else:
        #         #     pass
        #     # if mark != 0:
        #     #     m = 1
        # # return count# - m

        # # 一共有多少对括号？
        # # len(S) // 2

        # # 中间没有其它东西的括号有多少对？
        # # S.count(s)

        # print(count)
        # print(len(S) // 2)
        # print(S.count('()'))

        # return  count - ( len(S) // 2 - S.count('()') )

        positions = set()
        for k in range(1, len(S)):
            if S[k-1] == '(' and S[k] == ')':
                positions.add(k)
        # print(positions)
        mark = 0
        count = 0
        for k, s in enumerate(S):
            if s == '(':
                mark += 1
            else:
                mark -= 1
                if k in positions:
                    count += 1 * 2**mark
        return count

S = ''
S = "()"
S = "(())"
S = "()()"
S = "(()(()))"
S = "(()())"
S = "(())"
solu = Solution()
print(solu.scoreOfParentheses(S))