class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0
        # if len(s) == 1:
        #     return 1
        # count = 0
        # s0 = set()
        # max_ = 0
        # for letter in s:
        #     if letter not in s0:
        #         count += 1
        #         s0.add(letter)
        #     else:
        #         max_ = max(max_, count)
        #         count = 1
        #         s0.clear()
        #         s0.add(letter)
        # max_ = max(max_, count)
        # return max_
        if not s:
            return 0
        if len(s) == 1:
            return 1
        p, q = 0, 1
        ans = 1
        while q < len(s):
            while q < len(s) and len(s[p:q+1]) == len(set(s[p:q+1])):
                q += 1
            ans = max(ans, q-p)
            # if q != len(s):
            #     # print(1)
            #     ans = max(ans, q-p)
            #     # print(ans)
            # else:
            #     # print(-1)
            #     ans = max(ans, q-p)
            #     # print(ans)
            while p <= q and len(s[p:q+1]) != len(set(s[p:q+1])):
                p += 1
            # ans = max(ans, q-p)
            # if q != len(s):
            #     # print(2)
            #     ans = max(ans, q-p)
            #     # print(ans)
            # else:
            #     # print(-2)
            #     ans = max(ans, q-p)
            #     # print(ans)
        # print(p, q)
        return ans

# s = 'au'
# s = "dvdf"
# s = "abcabcbb"
# solu = Solution()
# print(solu.lengthOfLongestSubstring(s))