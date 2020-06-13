class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        a.reverse()
        b.reverse()
        length = max(len(a), len(b))
        if len(a) > len(b):
            for _ in range(length - min(len(a), len(b))):
                b.append('0')
        elif len(a) < len(b):
            for _ in range(length - min(len(a), len(b))):
                a.append('0')
        
        ans = []
        carry = 0
        for k in range(length):
            ans.append( str( (int(a[k]) ^ int(b[k])) ^ carry ) )
            # carry = ( int(a[k]) & int(b[k]) ) & carry
            carry = ( int(a[k]) & int(b[k]) ) | ( int(a[k]) & carry ) | ( carry & int(b[k]) )
        if carry:
            ans.append( str(carry) )
        return ''.join(reversed(ans))

solu = Solution()
a, b = '11', '1'
# a, b = '1010', '1011'
print(solu.addBinary(a, b))