class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # find pivot
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid

            # right sorted
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            # left sorted
            else:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1    

        return -1
