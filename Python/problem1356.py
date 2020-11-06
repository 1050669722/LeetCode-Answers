class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def howManyOne(num):
            cnt = 0
            while num:
                cnt += num % 2
                num //= 2
            return cnt

        def bit(num):
            if num == 0:
                return 0
            return bit(num >> 1) + (num & 1)

        # def softSort(x, y):
        #     if x[1] != y[1]:
        #         return x[1], y[1]
        #     else:
        #         return x[0], [0]

        arr.sort()

        # arr = list(map(lambda x: (x, howManyOne(x)), arr))
        arr = list(map(lambda x: (x, bit(x)), arr))

        arr.sort(key=lambda x: x[1])

        return [a[0] for a in arr]
        
