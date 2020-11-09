class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        for List in points:
            List.append(List[0]**2 + List[1]**2)
        points.sort(key=lambda x: x[2])
        return [List[:2] for List in points[:K]]
