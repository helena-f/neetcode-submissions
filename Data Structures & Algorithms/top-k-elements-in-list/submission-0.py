from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_array = Counter(nums)
        print(frequency_array)
        
        arr = []
        for num, count in frequency_array.items():
            arr.append([count, num])
        arr.sort()

        print(arr)

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

