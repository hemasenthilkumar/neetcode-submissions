class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        stack = []
        while i < len(tokens):
            if tokens[i] not in "+/*-":
                stack.append(int(tokens[i]))
            else:
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    if tokens[i] == "+":
                        stack.append(a+b)
                    elif tokens[i] == "-":
                        stack.append(b-a)
                    elif tokens[i] == "*":
                        stack.append(a*b)
                    elif tokens[i] == "/":
                        stack.append(int(b/a))
            i += 1
        return stack[0]