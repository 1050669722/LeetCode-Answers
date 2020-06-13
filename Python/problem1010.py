class Solution:
    def numPairsDivisibleBy60(self, time: list) -> int:
        # # ans = 0
        # # for p in range(len(time)):
        # #     for q in range(p+1, len(time)):
        # #         if (time[p] + time[q]) % 60 == 0:
        # #             ans += 1
        # # return ans

        # ans_1, ans_2 = 0, 0
        # time = [t%60 for t in time]
        # d = {}
        # # for k in range(len(time)):
        # #     if time[k] == 0:
        # #         try:
        # #             d[0]
        # #             ans += 1
        # #             d[0] = k
        # #         except:
        # #             d[0] = k
        # #     else:
        # #         try:
        # #             d[60-time[k]]
        # #             ans += 1
        # #         except:
        # #             d[time[k]] = k
        # # return ans
        # for t in time:
        #     try:
        #         d[t] += 1
        #     except:
        #         d[t] = 1
        # # print(d)
        # for t in d.keys():
        #     if t == 0 or t == 30:
        #         num = 1
        #         for n in range(1, d[t]+1):
        #             num *= n
        #         ans_1 += num//2
        #         # print(t, num//2)
        #     else:
        #         try:
        #             ans_2 += d[t]*d[60-t]
        #         except:
        #             pass
        # return ans_1 + ans_2//2

        # from collections import defaultdict
        # d = defaultdict(int)
        # d = {}
        # ans = 0
        # time = [x%60 for x in time]
        # for t in time:
        #     r = (60-t) % 60
        #     if r in d.keys():
        #         ans += d[r]
        #     else:
        #         d[t] += 1
        # return ans

        # 预处理：把数组中的元素全都模 60
        time = [t % 60 for t in time]

        from collections import defaultdict
        d = defaultdict(int)

        res = 0
        for t in time:
            # 1、先计数
            # 针对 [0, 0, 0] 这一类特殊用例，要模 60
            residue = (60 - t) % 60
            if residue in d:
                res += d[residue]

            # 2、再记录频数
            d[t] += 1

        return res

solu = Solution()
# time = [30,20,150,100,40]
time = [60, 60, 60]
print(solu.numPairsDivisibleBy60(time))
# solu.numPairsDivisibleBy60(time)