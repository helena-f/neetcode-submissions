class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketmap = {'(':')', '[': ']', '{': '}'}
        for ch in s:
            if ch in bracketmap:
                stack.append(ch)
            
            print(stack)
            if ch in bracketmap.values():
                if len(stack) == 0:
                    return False
                else:
                    stackchar = stack.pop()
                if bracketmap[stackchar] != ch:
                    return False
        if len(stack) != 0:
            return False
        return True
            