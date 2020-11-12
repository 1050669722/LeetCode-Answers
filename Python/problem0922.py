from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
#         OddInEvenInds, EvenInOddInds = [], []
#         for k in range(0, len(A), 2):
#             if A[k]%2 == 1:
#                 OddInEvenInds.append(k)
#         for k in range(1, len(A), 2):
#             if A[k]%2 == 0:
#                 EvenInOddInds.append(k)
#         for i in range(len(OddInEvenInds)):
#             A[OddInEvenInds[i]], A[EvenInOddInds[i]] = A[EvenInOddInds[i]], A[OddInEvenInds[i]]
#         return A

        # odd, even = [], []
        # for a in A:
        #     if a % 2 == 0:
        #         even.append(a)
        #     else:
        #         odd.append(a)
        # for i in range(len(A)):
        #     if i % 2 == 0:
        #         A[i] = even.pop()
        #     else:
        #         A[i] = odd.pop()
        # return A

        # ans = [0] * len(A)
        # i, j = 0, 1
        # for a in A:
        #     if a % 2 == 0:
        #         ans[i] = a
        #         i += 2
        #     else:
        #         ans[j] = a
        #         j += 2
        # return ans

        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 == 1:
                while A[j] % 2 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A      




