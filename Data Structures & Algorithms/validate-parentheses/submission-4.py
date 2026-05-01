class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = "({["
        for ch in s:
            if ch in opens:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (top == "(" and ch != ")") or (top == "{" and ch != "}") or (top == "[" and ch != "]"):
                    return False
        if stack:
            return False
        return True