class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for x,y in points:
            res.append([math.sqrt(x**2 + y**2), x, y])

        heapq.heapify(res)
        res = heapq.nsmallest(k, res)
        top = []

        for dist, x, y in res:
            top.append([x,y])
        return top
        