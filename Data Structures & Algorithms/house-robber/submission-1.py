class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [-1] * len(nums)
        def house(i):
            if i > len(nums) - 1:
                return 0
            if money[i] != -1:
                return money[i]
            money[i] = max(nums[i] + house(i+2), house(i+1))
            return money[i]
            
        return house(0)
            