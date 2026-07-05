class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #two pointers 
        # 1 1
        # z x y z x y z
        # 1   1
        # z x y z x y z
        # 1     1
        # z x y z x y z
        #   1     1
        # z x y z x y z
        #     1   1
        # z x y z x y z
        #     1     1
        # z x y z x y z

        # 1 1
        # a a a c a d 
        #   1 1  
        # a a a c a d 
        #     1 1
        # a a a c a d 
        # count = r - l + 1
        # algorithm:
        # 1. create set of characters seen. create const for max len seen
        # 2. using two pointers, use while loop. stop when right reaches the end 
        # 3. if no duplicate, move r forward. calculate curr len, update max. loop next
        #    if found duplicate, move l and r forward. loop next 
        # 4. return max len seen

        # 1 1
        # p w w k e w 
        # 1   1
        # p w w k e w 
        #   1 1
        # p w w k e w 
        #     1 1
        # p w w k e w 
        #     1     1
        # p w w k e w 
        # 
        n = len(s)
        if n == 0:
            return 0
        max_len = 1
        seen = {s[0]}

        l, r = 0, 1

        while r < n:            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            seen.add(s[r])
            r += 1
        return max_len
