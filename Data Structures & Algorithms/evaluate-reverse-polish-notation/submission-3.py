class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        value = 0
        
        operands = {'+': 1, '-': 2, '*':3, '/':4}

        for i in tokens:
            if i not in operands:
                stack.append(int(i))
            else:
                if stack:
                    val2 = stack.pop()
                    val1 = stack.pop()
                    if operands[i] == 1:
                        stack.append(val1 + val2)
                    elif operands[i] == 2:
                        stack.append(val1 - val2)
                    elif operands[i] == 3:
                        stack.append(val1 * val2)
                    else:
                        stack.append(int(val1 / val2))
        return stack.pop()