from typing import List

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # A = [str(x) for x in A]
        # A = ''.join(A)
        # A = int(A)
        # A += K
        # A = str(A)
        # A = [x for x in A]
        # A = [int(x) for x in A]
        # return A

        num = []
        while K:
            tmp = K%10
            num.append(tmp)
            K //= 10
        num.reverse()
        # print(num)

        ans = []
        carry = 0
        while A and num:
            tmp = A.pop() + num.pop() + carry
            ans.append(tmp % 10)
            carry = tmp // 10
        if A:
            while A:
                tmp = A.pop() + carry
                ans.append(tmp % 10)
                carry = tmp // 10
            if carry:
                ans.append(carry)
        elif num:
            while num:
                tmp = num.pop() + carry
                ans.append(tmp % 10)
                carry = tmp // 10
            if carry:
                ans.append(carry)
        elif carry:
            ans.append(carry)
        ans.reverse()
        return ans

# solu = Solution()
# A, K = [2,1,5], 806
# A, K = [9,9,9,9,9,9,9,9,9,9], 1
# print(solu.addToArrayForm(A, K))