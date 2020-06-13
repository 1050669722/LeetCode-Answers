class Solution:
    def longestPalindrome(self, s: str) -> int:
        # d = {}
        # for c in s:
        #     try:
        #         d[c] += 1
        #     except:
        #         d[c] = 1
        # ans = 0
        # mark = 0
        # for value in d.values():
        #     ans += value//2 * 2
        #     if value%2 == 1:
        #         mark += 1
        # if mark != 0:
        #     ans += 1
        # return ans

        # def __call__(self):
        from collections import Counter
        d = Counter(s)
        ans = 0
        mark = 0
        for value in d.values():
            ans += value//2 * 2
            if value%2 == 1:
                mark += 1
        if mark:
            ans += 1
        return ans



solu = Solution()
s = "abccccdd"
s = "ccc"
print(solu.longestPalindrome(s))


# #以下方法只需要O(1)的额外空间
# class Solution:
#     def longestPalindrome(self, s):
#         ans = 0
#         for v in collections.Counter(s).itervalues():
#             ans += v / 2 * 2
#             if ans % 2 == 0 and v % 2 == 1:
#                 ans += 1
#         return ans

# # 作者：LeetCode
# # 链接：https://leetcode-cn.com/problems/longest-palindrome/solution/zui-chang-hui-wen-chuan-by-leetcode/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
