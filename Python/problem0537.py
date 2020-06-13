class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a, b = a.split('+'), b.split('+')
        a_real, a_imag = int(a[0]), int(a[1][:-1])
        b_real, b_imag = int(b[0]), int(b[1][:-1])
        ans = [ str(a_real*b_real-a_imag*b_imag), '+', str(a_real*b_imag+b_real*a_imag)+'i' ]
        return ''.join(ans)

a, b = "1+1i", "1+1i"
a, b = "1+-1i", "1+-1i"
solu = Solution()
print(solu.complexNumberMultiply(a, b))