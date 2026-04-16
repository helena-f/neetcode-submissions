class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        currlen = 0

        left = right = 0
        while right < len(s) and left < len(s):
            # print(left,right)
            if s[right] not in s[left:right]:
                right += 1
                currlen += 1
                print(currlen)
                maxlen = max(currlen, maxlen)
            else: 
                left += 1
                currlen -= 1

        return maxlen