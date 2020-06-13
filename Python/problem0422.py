from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m = len(words)
        n = 0
        for word in words:
            n = max(n, len(word))
        
        for k in range(len(words)):
            words[k] = list(words[k])
            for _ in range(n-len(words[k])):
                words[k].append('0')

        # print(words)

        # for k in range(min(m, n)):
        #     a = words[k]
        #     b = []
        #     for word in words:
        #         b.append(word[k])
        #     if a != b:
        #         return False
        # return True

        trans_words = [ [r[c_ind] for r in words] for c_ind in range(n) ]
        for k in range(min(m, n)):
            a = words[k]
            b = trans_words[k]
            if a != b:
                return False
        return True


solu = Solution()
words = [
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
words = [
  "abcd",
  "bnrt",
  "crm",
  "dt"
]
# words = [
#   "ball",
#   "area",
#   "read",
#   "lady"
# ]
print(solu.validWordSquare(words))