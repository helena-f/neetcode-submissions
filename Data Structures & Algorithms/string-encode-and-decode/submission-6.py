class Solution:

    def encode(self, strs: List[str]) -> str:
        # if not strs:
        #     return ""
        res = ""
        for substr in strs:
            res += str(len(substr)) + "#" + substr
        
        print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        strsize = len(s)
        i = 0
        while i < strsize:
            j = i
            while s[j] != '#':
                j+= 1
            
            wordlen = int(s[i:j])

            i = j + 1
            j = i + wordlen
            res.append(s[i:j])
            i = j

        return res