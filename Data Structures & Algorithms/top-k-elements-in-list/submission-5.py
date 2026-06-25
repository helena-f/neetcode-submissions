from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        # get frequencies 
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1

        res = sorted(hm.keys(), key =lambda x: hm[x], reverse=True)
        
        return res[:k]

        

