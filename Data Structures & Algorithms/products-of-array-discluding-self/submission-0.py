class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [],[]
        prefix_total = 1
        suffix_total = 1

        if not nums:
            return []

        size = len(nums)
        for i in range(size):
            suffix_index = size - i - 1
            
            prefix_total = nums[i] * prefix_total
            prefix.append(prefix_total)

            suffix_total = nums[suffix_index] * suffix_total
            suffix.append(suffix_total)

        suffix.reverse()

        print(prefix)
        print(suffix)
        output = []
        for i in range(size):
            total_mult = 1
            print("finding for index: ", i)
            if i-1 >= 0:
                total_mult *= prefix[i-1]
                print("prefix ", prefix[i-1])
            if i+1 < size:
                total_mult *= suffix[i+1]
                print("suffix ",suffix[i+1])

            output.append(total_mult)

        return output
