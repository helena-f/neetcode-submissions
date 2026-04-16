class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s).lower()
        print(s)
        left, right = 0,0

        size = len(s)
        if size % 2 == 0:
            left = int(size/2) -1
            right = int(size/2)
        else:
            left = right = int(size/2)

        print(left, right)

        while left >= 0 and right < size:
            if s[left] != s[right]:
                print(s[left], s[right])
                return False
            left -= 1
            right += 1
        return True