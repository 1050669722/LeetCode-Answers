class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if not self.fun(A, B, C, D, E, F, G, H):
            return (C-A)*(D-B) + (G-E)*(H-F)
        intersection = ( min(D, H) - max(B, F) ) * ( min(C, G) - max(A, E) )
        return (C-A)*(D-B) + (G-E)*(H-F) - intersection
    def fun(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        mark = False
        if by1 < ay2 and by2 > ay1 and bx1 < ax2 and bx2 > ax1:
            mark = True
        return mark

solu = Solution()
A, B, C, D, E, F, G, H = -2, -2, 2, 2, 3, 3, 4, 4
print(solu.computeArea(A, B, C, D, E, F, G, H))