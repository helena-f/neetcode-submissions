class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for x,y in points:
            res.append([x**2 + y**2, x, y])

        heapq.heapify(res)
        top = []
        while k > 0 and len(res) > 0: 
            elt = heapq.heappop(res)
            top.append([elt[1], elt[2]])
            k -= 1
        return top
        