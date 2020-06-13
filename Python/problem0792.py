class Solution:
    def numMatchingSubseq(self, S, words):
        ans = 0
        for word in words:
            ans += self.fun(word, S)
        return ans
    def fun(self, word, S):
        if not word:
            return 1
        if not S:
            return 0
        # ind_w = 0
        ind_S = 0
        # while ind_w<len(word) and ind_S<len(S):
        #     if S[ind_S] == word[ind_w]:
        #         ind_w += 1
        #     ind_S += 1
        # # if ind_w == len(word):
        # #     print(word)
        # return int(ind_w == len(word))
        for ind_w in range(len(word)):#while ind_w < len(word):
            res = S.find(word[ind_w], ind_S)
            if res == -1:
                return 0
            else:
                ind_S = res + 1
        print(word)
        return 1

# solu = Solution()
# S = "abcde"
# words = ["a","bb","acd","ace"]
# print(solu.numMatchingSubseq(S, words))
