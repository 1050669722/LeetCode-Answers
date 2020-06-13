class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        mark = False
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        if by1 < ay2 and by2 > ay1 and bx1 < ax2 and bx2 > ax1:
            mark = True
        return mark
