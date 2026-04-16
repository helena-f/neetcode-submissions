class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return []

        def backtrack(curr, nums):
           
            for i in range(len(nums)):
                curr.append(nums[i])
                res.append(curr[:])
                backtrack(curr, nums[1+i:])
                curr.pop()

        
        arr = []
        backtrack(arr, nums)
        res.append([])
        return res