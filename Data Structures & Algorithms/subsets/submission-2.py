class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return []

        arr = []
        def backtrack( i):
            # out of bounds
            if i >= len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[i])
            backtrack(i+1)
            arr.pop()
            backtrack(i+1)
            
        backtrack( 0)
        return res