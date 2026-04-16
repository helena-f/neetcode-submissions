class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # keep a min heap of the k largest elements, so the minimum elt is 
        # the elt that would be switched out if a larger element is found

        heap = []

        for n in nums:
            heapq.heappush(heap, n)

            if len(heap) > k: 
                heapq.heappop(heap)

        return heap[0]
