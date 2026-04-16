class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        # keep a max-heap for k closest distances
        # compare to the top element. if the top element is closer, don't
        # modify the heap
        # if the top element is further, push the new closest elt
        heapq.heapify(res)

        for x, y in points:
            curr_dist = -1 * (x**2 + y**2)
            heapq.heappush(res, [curr_dist, x, y])

            if len(res) > k:
                heapq.heappop(res)


        return [[x,y] for dist, x, y in res]
        