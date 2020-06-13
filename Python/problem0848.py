from typing import List

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        sum_ = 0 #shifts[-1]
        for k in range(len(shifts)-1, -1, -1):
            tmp = shifts[k]
            shifts[k] += sum_
            sum_ += tmp
        S = list(S)
        for k, shift in enumerate(shifts):
            # print((ord(S[k])+shift)%26)
            S[k] = chr((ord(S[k])+shift-ord('a'))%26+ord('a'))
        # print(S)
        return ''.join(S)

S = "abc"; shifts = [3,5,9]
solu = Solution()
print(solu.shiftingLetters(S, shifts))