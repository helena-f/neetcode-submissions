class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        keyhash = {}
        for i in nums:
            keyhash[i] = i

        longest = 0
        for i in keyhash:
            if (i - 1) not in keyhash:
                currlen = 1
                while (i + currlen) in keyhash:
                    currlen += 1
                longest = max(currlen, longest)

        return longest