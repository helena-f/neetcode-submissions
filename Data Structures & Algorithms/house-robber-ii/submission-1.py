class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        money = [-1] * len(nums)
        money2 = [-1] * len(nums)
        def house(mon, i, flag):
            if i >= len(nums) or (flag and i == len(nums)-1):
                return 0

            if mon[i] != -1:
                return mon[i]
            mon[i] = max(nums[i] + house(mon, i+2, flag or (i==0)), house(mon, i+1,flag))
            return mon[i]

        return max(house(money, 0, True), house(money2, 1,False))