class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
    #     d = self.reset()
    #     # print(d)
    #     ans = 0
    #     for t in text:
    #         try:
    #             d[t] -= 1
    #             if self.isempty(d):
    #                 ans += 1
    #                 d = self.reset()
    #         except:
    #             pass
    #     return ans

    # def reset(self):
    #     word = 'balloon'
    #     d = {}
    #     for c in word:
    #         try:
    #             d[c] += 1
    #         except:
    #             d[c] = 1
    #     return d

    # def isempty(self, d):
    #     sum_ = 0
    #     for value in d.values():
    #         sum_ += value
    #     if sum_ == 0:
    #         return True
        
        d = {}
        for c in 'balloon':
            d[c] = 0
        for t in text:
            try:
                d[t] += 1
            except:
                pass
        d['l'] //= 2
        d['o'] //= 2
        return min(d.values())


solu = Solution()
text = 'loonbalxballpoon'
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
print(solu.maxNumberOfBalloons(text))