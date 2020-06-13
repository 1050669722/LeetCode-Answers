class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # if S == '-':
        #     return S
        # if len(S) == 1:
        #     return S.upper()
        # # print(1)
        # # s = list(S)
        # # try:
        # if '-' in S:
        #     # print(s)
        #     # s.index('-')
        #     for k in range(len(S)):
        #         if S[k] != '-':
        #             break
        #     S = S[k:]
        #     S = S.split('-')
        #     ans = S[0].upper()
        #     S = S[1:]
        #     tmp = ''.join(S)
        #     num = len(tmp) % K
        #     ans += tmp[:num]
        #     tmp = tmp[num:]
        #     ans += '-'
        #     for k in range(len(tmp)):
        #         ans += tmp[k].upper()
        #         if (k+1) % K == 0:
        #             ans += '-'
        #     return ans[:-1].upper()
        
        # # except:
        # else:
        #     ans = []
        #     S = list(S)
        #     count = 0
        #     for k in range(len(S)-1, -1, -1):
        #         ans.append(S[k].upper())
        #         if (count+1) % K == 0:
        #             ans.append('-')
        #         count += 1
        #     return ''.join(reversed(ans[:-1])).upper()

        tmp = []
        for s in S:
            if s != '-':
                tmp.append(s)
        # print(tmp)
        count = 0
        ans = []
        for k in range(len(tmp)-1, -1, -1):
            ans.append(tmp[k])
            if (count+1) % K == 0:
                # print(count+1)
                ans.append('-')
            count += 1
            # print(ans)
        # print(ans)
        return ''.join(reversed(ans)).upper().strip('-')


solu = Solution()
S, K = "5F3Z-2e-9-w", 4
# S, K = "2-5g-3-J", 2
# S, K = "aaaa", 2
# S, K = "abc-abc", 3
S, K = "--a-a-a-a--", 2
# S, K = "a0001afds-", 4
print(solu.licenseKeyFormatting(S, K))