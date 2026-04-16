class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subarray = []

        def dfs(i, currsum):
            if currsum == target:
                res.append(subarray[:])
                return
            
            if i >= len(nums) or currsum > target:
                return

            # add self again
            subarray.append(nums[i])
            dfs(i, currsum + nums[i])
            subarray.pop()

            # don't add anything, move on
            dfs(i + 1, currsum)

        dfs(0, 0)
        return res