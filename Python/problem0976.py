class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        perimeter = 0
        A.sort(reverse=True)
        for k in range(len(A)-2):
            if self.fun(A[k], A[k+1], A[k+2]):
                perimeter = max(perimeter, A[k] + A[k+1] + A[k+2])
                return perimeter
        return perimeter

    def fun(self, a, b, c):
        # if a+b>c and a+c>b and b+c>a:
        if b+c>a:
            return True
        else:
            return False


