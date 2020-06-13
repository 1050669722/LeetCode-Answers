class Solution:
    def mySqrt(self, x: int) -> int:
        head, tail = 0, x
        mid = (head + tail) // 2
        while head < tail:
            if mid**2 < x:
                head = mid + 1
                mid = (head + tail) // 2
            elif mid**2 > x:
                tail = mid - 1
                mid = (head + tail) // 2
            else:
                return mid
        head -= 1
        tail += 1
        smallest = abs(head**2 - x)
        ans = 0
        tmp = [head, mid, tail]#[abs(mid**2-x), abs(tail**2-x)]
        # print(tmp)
        for k in range(len(tmp)):
            if tmp[k]**2 <= x and abs(tmp[k]**2 - x) < smallest:
                smallest = abs(tmp[k]**2 - x)
                ans = k
        ans = tmp[ans]
        print(ans)
        if abs((ans-1)**2 - x) < 1:
            ans -= 1
        return ans

solu = Solution()
x = 8
print(solu.mySqrt(x))