class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float("inf")

            end = min(len(nums), nums[i] + i + 1)
            currmin = float("inf")
            for j in range(i + 1, end):
                currmin = min(currmin, 1 + dp(j))
            memo[i] = currmin
            return currmin
        return dp(0)