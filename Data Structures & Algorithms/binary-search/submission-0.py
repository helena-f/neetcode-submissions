class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        m = 0

        while left < right:
            m = int((left + right ) / 2)
            print(m)
            if nums[m] == target:
                return m
            
            if nums[m] > target:
                right = m
            if nums[m] < target:
                left = m+1

        return -1