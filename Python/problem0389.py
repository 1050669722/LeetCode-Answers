class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # s, t = [x for x in s], [x for x in t]
        # s.sort(), t.sort()
        # for k in range(len(s)):
        #     if t[k] != s[k]:
        #         return t[k]
        # return t[-1]

        sum_s, sum_t = 0, 0
        for s0 in s:
            sum_s += ord(s0)
        for t0 in t:
            sum_t += ord(t0)
        return chr(sum_t - sum_s)
