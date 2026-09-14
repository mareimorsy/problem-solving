class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for t in tokens:
            if t in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                # print(a, b)
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(b - a)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    stack.append(int(b / a))

            else:
                stack.append(t)
        return int(stack.pop())
            
