class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        while left < right:
            m = int((left + right) / 2)
            print(m, nums[m])
            if nums[m] < nums[right]:
                right = m
            else:
                left = m +1

        return nums[left]