class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s
        
        # stack = list(s[:k-1])
        # for p in range(k-1, len(s)):
        #     # print(stack)
        #     if len(stack) >= k-1 and s[p] == stack[-1] and len(set(stack[-(k-1):])) == 1:
        #         # for _ in range(k-1):
        #         #     stack.pop()
        #         # 要pop这么多次，不如做切片，但是这样做还是会TLE
        #         stack = stack[:-(k-1)]
        #     else:
        #         stack.append(s[p])
        # return ''.join(stack)

        # s += '.'
        # count = 1
        # stack, tmp = [], [s[0]]
        # for t in range(1, len(s)):
        #     # print(s[t])
        #     # print(tmp)
        #     if not tmp or s[t] == tmp[-1]:
        #         count += 1
        #         tmp.append(s[t])
        #     else:
        #         stack.extend(tmp)
        #         # print(stack)
        #         count = 1
        #         tmp = [s[t]]
        #     if count == k:
        #         count = 0
        #         tmp.clear()
        # return ''.join(stack)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        ans = ""
        for c, l in stack:
            ans += c * l
        return ans

# 作者：smoon1989
# 链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii/solution/zhan-python3-by-smoon1989/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# s = "abcd"; k = 2
# s = "abcdd"; k = 2
s = "deeedbbcccbdaa"; k = 3
# s = "pbbcggttciiippooaais"; k = 2
# s = "deeedbbcccbdaa"; k = 3
solu = Solution()
print(solu.removeDuplicates(s, k))