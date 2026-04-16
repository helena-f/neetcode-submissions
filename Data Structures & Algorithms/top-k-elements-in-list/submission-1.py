from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get frequencies
        frequency_array = Counter(nums)
        print(frequency_array)
        
        # sort the frequencies
        arr = []
        for num, count in frequency_array.items():
            arr.append([count, num])
        arr.sort(reverse=False)

        print(arr)


        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res

