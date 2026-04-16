class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsmap = {}
        for i, n in enumerate(nums):
            numsmap[n] = i
        
        for i, n in enumerate(nums):
            complement = target - n
            if complement in numsmap and numsmap[complement] != i:
                return [i, numsmap[complement]]
            
        return None