class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subarray = []

        candidates.sort()
        def dfs(i, currsum):
            if currsum == target:
                res.append(subarray[:])
                return
            
            if currsum > target or i == len(candidates):
                return

            subarray.append(candidates[i])
            dfs(i+1, currsum + candidates[i])
            subarray.pop()
            # currelt = candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, currsum)
        dfs(0,0)
        return res
