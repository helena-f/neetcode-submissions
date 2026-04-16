import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        topk = heapq.nlargest(self.k, self.heap)
        return topk[-1]
